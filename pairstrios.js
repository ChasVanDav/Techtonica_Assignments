let cohort = [
  "Ami Lian",
  "Ayia Asylbek kyzy",
  "Courey Jimenez",
  "Leah Putlek",
  "Mai Thanh Mai",
  "Nina Simmons",
  "Steph McPeters-Esparza",
  "Thane Wilson",
  "Vanessa Davis",
  "Winnie Kelley",
  "Juliana Snorek",
]

// Shuffle the array
function shuffle(array) {
  var currentIndex = array.length,
    randomIndex

  // While there remain elements to shuffle...
  while (currentIndex !== 0) {
    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex)
    currentIndex--

    // And swap it with the current element.
    ;[array[currentIndex], array[randomIndex]] = [
      array[randomIndex],
      array[currentIndex],
    ]
  }
  return array
}

// Will create 2x groups of 4 and 2x groups of 3
// good for 14 person cohort
function createTrioPairs() {
  let shuffledArray = shuffle(cohort)

  console.log("Groups of Trios:")
  console.log("Group 1:", shuffledArray[0], shuffledArray[1], shuffledArray[2])
  console.log("Group 2:", shuffledArray[3], shuffledArray[4], shuffledArray[5])
  console.log("Group 3:", shuffledArray[6], shuffledArray[7], shuffledArray[8])
  console.log(
    "Group 4:",
    shuffledArray[9],
    shuffledArray[10],
    shuffledArray[11]
  )
}

createTrioPairs()

// If there are not enough participants to pair each group with three people, break groups into two person pairs
function createPairs() {
  let shuffledArray = shuffle(cohort)

  console.log("Groups of Pairs:")
  console.log("Group 1:", shuffledArray[0], shuffledArray[1])
  console.log("Group 2:", shuffledArray[2], shuffledArray[3])
  console.log("Group 3:", shuffledArray[4], shuffledArray[5])
  console.log("Group 4:", shuffledArray[6], shuffledArray[7])
  console.log("Group 5:", shuffledArray[8], shuffledArray[9])
  console.log("Group 6:", shuffledArray[10], shuffledArray[11])
}

createPairs()
