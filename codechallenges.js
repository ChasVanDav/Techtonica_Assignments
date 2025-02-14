// ====================== Problem 1 ============================

// Given an input string, reverse the string word by word, the first word will be the last, and so on.

// Examples
// reverseWords(" the sky is blue") ➞ "blue is sky the"

// reverseWords("hello   world!  ") ➞ "world! hello"

// reverseWords("a good example") ➞ "example good a"

//pseudo coding
//split('').reverse.join('') --> similar but instead of by character, by space --> split(' ').reverse.join(' ')

// function reverseWords(str) {
//   return str.split(" ").reverse().join(" ")
// }

// console.log(reverseWords("hello world!"))

// ====================== Problem 2 ============================
//  If you get through the first problem, move onto this problem
// =============================================================

// Prompt1:
// Write a function that takes an array of strings as input and returns a new array where the first element is moved to the end of the array. You must use both shift and push methods to achieve this.

// Prompt 2:
// Write a function that takes an array of numbers as input and returns a new array where the last element is moved to the beginning of the array. You must use both pop and unshift methods to achieve this.

/*
Write a function that takes an array of strings and a string item as input. 
The function should remove the first occurrence of item from the array and then add it to the end of the array. 
You must use both shift and push methods to achieve this.
*/

//methods: shift - removes item of 0 index of array & push - adds item to last index of array
let array = ["hello", "world", "javascript", "coding"]

function lastFirst(arr) {
  let newArr = arr.slice() //or [...arr]
  let shifted = newArr.shift()
  newArr.push(shifted)
  return newArr
}

console.log("feb12 cc #1 (control): ", array)
console.log("feb12 cc #1: ", lastFirst(array))

/*
Write a function that takes an array of numbers as input and returns a new array with all duplicate numbers removed. 
You must use reduce and push methods to achieve this.
*/
let numArray = [1, 2, 4, 3, 4, 2, 3, 6, 8]

function removeDupes(arr) {
  let array = arr.slice()

  let newArray = array.reduce((accumulator, item) => {
    if (!accumulator.includes(item)) {
      accumulator.push(item)
    }
    return accumulator
  }, [])

  return newArray
}

console.log("feb12 cc #2: ", removeDupes(numArray))


