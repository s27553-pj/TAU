import { Before, After, setDefaultTimeout } from "@cucumber/cucumber";
import { Builder } from "selenium-webdriver";

setDefaultTimeout(60 * 1000);

Before(async function () {
    const browser = process.env.BROWSER || "chrome";
    this.browser = browser;

    console.log(`[SETUP] Start: ${browser}`);
    this.driver = await new Builder().forBrowser(browser).build();
});

After(async function () {
    console.log(`[TEARDOWN] Quit: ${this.browser}`);
    if (this.driver) await this.driver.quit();
});
