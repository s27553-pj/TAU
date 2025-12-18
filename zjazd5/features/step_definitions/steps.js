import { Given, When, Then } from "@cucumber/cucumber";
import { By, Key, until } from "selenium-webdriver";

Given("Otwieram stronę {string}", async function (url) {
    console.log(`[STEP] Open: ${url}`);
    await this.driver.get(url);
    await this.driver.wait(until.elementLocated(By.css("body")), 15000);
});

When("Wyszukuję frazę {string}", async function (text) {
    console.log(`[STEP] Search: ${text}`);
    const input = await this.driver.wait(
        until.elementLocated(By.css("#searchInput")),
        15000
    );
    await input.clear();
    await input.sendKeys(text, Key.ENTER);
});

Then("Widzę nagłówek artykułu {string}", async function (title) {
    const h = await this.driver.wait(
        until.elementLocated(By.css("h1#firstHeading span.mw-page-title-main")),
        15000
    );
    const text = (await h.getText()).trim();

    if (text !== title) {
        throw new Error(`Oczekiwano "${title}", otrzymano "${text}"`);
    }
});


When("Zmieniam język na {string}", async function (lang) {
    console.log(`[STEP] Change language: ${lang}`);

    // 1) spróbuj kliknąć polski link po atrybucie lang="pl"
    try {
        const pl = await this.driver.wait(
            until.elementLocated(By.css('a[lang="pl"]')),
            7000
        );
        await pl.click();
        return;
    } catch (e) {
        // 2) fallback: wejście bezpośrednio
        const current = await this.driver.getCurrentUrl();
        const url = new URL(current);
        await this.driver.get(`https://pl.wikipedia.org/wiki/${url.pathname.split("/").pop()}`);
    }
});

When("Klikam link {string}", async function (text) {
    const link = await this.driver.wait(
        until.elementLocated(By.partialLinkText(text)),
        15000
    );
    await link.click();
});

When("Przechodzę na stronę {string}", async function (path) {
    const current = await this.driver.getCurrentUrl();
    const url = new URL(current);
    await this.driver.get(`${url.origin}${path}`);
});

Then("Adres URL zawiera {string}", async function (part) {
    await this.driver.wait(async () => {
        const url = await this.driver.getCurrentUrl();
        return url.includes(part);
    }, 15000);

    const finalUrl = await this.driver.getCurrentUrl();
    console.log(`[ASSERT] URL contains: ${part} | current: ${finalUrl}`);
});


Then("Widzę na stronie tekst {string}", async function (text) {
    const source = await this.driver.getPageSource();
    if (!source.includes(text)) {
        throw new Error(`Nie znaleziono tekstu "${text}"`);
    }
});
