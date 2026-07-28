const { expect, test } = require("@playwright/test");

test("navigation exposes only CV-backed site sections", async ({ page }) => {
  await page.goto("/", { waitUntil: "networkidle" });

  const labels = await page.locator(".nav-menu .nav-link").allTextContents();
  expect(labels.map((label) => label.trim())).toEqual(["Publications", "Talks", "Teaching"]);

  await expect(page.getByRole("link", { name: "blog", exact: true })).toHaveCount(0);
  await expect(page.getByRole("link", { name: "repositories", exact: true })).toHaveCount(0);
  await expect(page.getByRole("link", { name: "CV", exact: true })).toHaveCount(0);
});

test("home has one contact email, one CV link, and no profile image", async ({ page }) => {
  await page.goto("/", { waitUntil: "networkidle" });

  await expect(page.locator('a[href="mailto:jaeyoungkim22@snu.ac.kr"]')).toHaveCount(1);
  await expect(page.locator('a[href$="/assets/pdf/CV_Jaeyoung_Kim.pdf"]')).toHaveCount(1);
  await expect(page.locator("main img")).toHaveCount(0);
  await expect(page.getByText("Selected publications", { exact: false })).toHaveCount(0);
});

test("publication abstract expands without exposing BibTeX", async ({ page }) => {
  await page.goto("/publications/", { waitUntil: "networkidle" });

  const abstract = page.locator(".publication-abstract").first();
  await expect(abstract).not.toHaveAttribute("open", "");
  await abstract.locator("summary").click();
  await expect(abstract).toHaveAttribute("open", "");
  await expect(abstract.locator("p")).toContainText("quantum channels of rank at most three");

  await expect(page.locator('a[href^="https://doi.org/"]')).toHaveCount(1);
  await expect(page.locator('a[href^="https://arxiv.org/"]')).toHaveCount(1);
  await expect(page.getByText("BibTeX", { exact: false })).toHaveCount(0);
});

test("teaching contains only entries synchronized from the CV", async ({ page }) => {
  await page.goto("/teaching/", { waitUntil: "networkidle" });

  await expect(page.locator(".teaching-list li")).toHaveCount(8);
  await expect(page.getByText("Differential and Integral Calculus Practice", { exact: false })).toBeVisible();
  await expect(page.getByText("Teaching Volunteer", { exact: false })).toBeVisible();
  await expect(page.getByText("Machine Learning", { exact: false })).toHaveCount(0);
  await expect(page.getByText("Data Science", { exact: false })).toHaveCount(0);
});
