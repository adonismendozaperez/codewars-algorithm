//  isLucky
/*  Ticket numbers usually consist of an even number of digits.
    A ticket number is considered lucky if the sum of the first 
    half of the digits is equal to the sum of the second half.

    Given a ticket number n, determine if it's lucky or not.
 */

function isLucky(n) {
    let numbers = (n+'').split('');
    let firstH = numbers.slice(0, numbers.length/2).reduce(
        (a, c) => parseInt(a)+ parseInt(c)
    )
    
    let secondtH = numbers.slice(numbers.length/2, numbers.length).reduce(
        (a, c) => parseInt(a)+ parseInt(c)
    )
    
    return firstH == secondtH
}