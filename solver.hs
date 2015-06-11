import Data.List

-- note that the 9 x 9 board is numbered sequentially from left to right,
-- top to bottom using 0..80.  Thus , the rowNo of cells 0..8 is 0,
-- 9..17 is 1, etc.  colNo is similar, except that colNo of 0, 9, ... is 0,
-- 1, 10, ... is 1, etc.

rowNo  sq =  sq `div` 9

colNo  sq =  sq `mod` 9

boxNo  sq =  (sq `div` 9 `div` 3 ) * 3
    + (sq `div` 3) `mod` 3

-- Two squares sq1 and sq2 are in the same neighborhood if their row,
-- column, or box numbers are the same.

isNeighbor sq1 sq2 =
    ((rowNo sq1) == (rowNo sq2)) ||
    ((colNo sq1) == (colNo sq2)) ||
    (((boxNo sq1) == (boxNo sq2)))

-- update neighbor candiadte list in cell2 by deleting the only candidate value
-- in cell1 from the candidate list in cell2 if both are
-- neighbors; otherwise cell2 is left alone.

-- type Value = Int
type Cell = (Int, [Int])
type Board = [Cell]

----------- solution goes here --------------

update c1 c2
	| length (snd c2) == 1	= c2 
	| isNeighbor (fst c1) (fst c2) = (fst c2, delete (head (snd c1)) (snd c2))
	| otherwise = c2 

updateb	c1 b
	| null (tail b) = [update c1 (head b)]
	| otherwise = (update c1 (head b)): (updateb c1 (tail b))
	
solcand  b
	| b == [] = b
	| length (snd (head b)) == 1 = (head b):(solcand (tail b))
	| otherwise = solcand (tail b)

unsol b
	| b == [] = b
	| length (snd (head b)) > 1 = (head b):(unsol (tail b))
	| otherwise = unsol (tail b)

forall cell b
	| cell == [] = b
	| otherwise = forall (tail cell) (updateb (head cell) b)


solvem bd
	| unsol bd == [] = bd
	| otherwise = solvem (forall (solcand bd) bd)
 

----------- your soltion ends here ---------------
-- given a valid board, computes the one and only solution.
-- all the real work is done by solvem
-- code was added to solve to convert the board to 
-- a list of digits in square order
solve :: [Int] -> [Int]
solve bd = [head (snd x) | j <- [0..80], x <- ans , j == fst x]
    where
        ans = solvem (list2bd bd)

-- list2bd :: [Int] -> Board
list2bd xs = [ (i, cand (xs!!i)) | i <- [0..80] ]
    where 
        cand y = if y > 0 then [y] else [1..9]
    
