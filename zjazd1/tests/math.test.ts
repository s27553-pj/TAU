import { describe, it, expect} from "vitest";
import {add, multiply, divide, calculateCircleArea} from "../src/math";
describe("Math", () => {
    it("returns 5 when addind 2 and 3 ", () => {
        expect(add(2,3)).toBe(5);
    });
    it("works with negative numbers", () => {
        expect(add(-2,3)).toBe(1)
    })
    it("multiplies numbers", () => {
        expect(multiply(3,4)).toBe(12);
    })
    it("divides numbers", () => {
        expect(divide(15,5)).toBe(3);
    })
    it("returns an error when dividing by zero", ()  => {
        expect(() => divide(15,0)).toThrow("Division by zero");
        })
    it("returns a value close to 314.16 when radius is 10", () => {
        expect(calculateCircleArea(10)).toBeCloseTo(314.16, 2);
    })
})