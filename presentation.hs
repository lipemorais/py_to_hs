import Prelude hiding (elem, map)

elem :: Eq a => a -> [a] -> Bool
elem _ []       = False
elem x (y:ys)
    | x == y    = True
    | otherwise = elem x ys

factorial :: Int -> Int
factorial 1 = 1
factorial x = x * factorial(x-1)

factorial' :: Int -> Int
factorial' x = foldr (*) 1 [1..x]

factorial'' :: Int -> Int
factorial'' x = if x == 1
    then 1
    else x * factorial'' (x-1)

map :: (a -> a) -> [a] -> [a]
map _ [] = []
map f (x:xs) = f x : map f xs

-- Quicksort
quicksort :: Ord a => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = quicksort small ++ [x] ++ quicksort large
    where small = [y | y <- xs, y <= x]
          large = [y | y <- xs, y > x]

-- Reverse Words
reverseWords :: String -> String
reverseWords = unwords . map reverse . words
