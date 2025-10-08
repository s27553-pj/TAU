import { describe, it, expect} from "vitest";
import {capitalize} from "../src/textUtilis";
describe("text", function() {
    it("capitalizes the first letter of a word",()=> {
        expect(capitalize("hej")).toMatch(/^[A-Z]/);
    })
    it("retuns true if string has letter H", () => {
        expect(capitalize("hej")).toContain("H");
    })
})
