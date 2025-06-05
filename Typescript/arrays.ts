// we will explore arrays in typescript
// Arrays in TypeScript can be defined using the type followed by square brackets
// or using the Array type with generics.
// Here are some examples of how to define and use arrays in TypeScript:

// 1. Defining an array of numbers
let ids:number[] = [11,12,113,123,1234,1278];
let ids2:Array<number> = [11,12,113,123,1234,1278];
let stringArray:string[] = ["apple","banana","peru"];
let stringArray2 : string[] =  new Array("bmw","jetair","porsche")//imp for tricks
let  create : number[] = Array.of(34); // imp for tricks
console.log("ids2" + ids.length); //imp for tricks



//2. iteration over the arrays

//basic for loop
for(let i=0;i<ids.length;i++){
    console.log(ids[i]);
} // imp for tricks

//foreach for arrays
ids.forEach((i)=> {console.log(i+2)}) // extremely impportant cause its mostly used 

//Array methods

