import {describe, it, expect} from "vitest";
import {contains} from "../src/arrayUtilis";
describe("array", function() {
    it("returns true when element is in array",() => {
        expect(contains([1,2,3],2)).toBeTruthy();
    })
    it("returns false when element is not in array",() => {
        expect(contains([1,2,3],5)).toBeFalsy();
    })
})