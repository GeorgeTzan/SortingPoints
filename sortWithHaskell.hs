import System.Environment
import Text.Printf
import Data.List
import Data.Function
import System.CPUTime

type Point = (Double, Double, Double)

distance :: Point -> Double
distance (x,y,z) = sqrt(x*x+y*y+z*z)

readPoints :: FilePath -> IO [Point]
readPoints filename = do
    contents <- readFile filename
    let linesOfContents = lines contents
    let readPoint line = let x:y:z:_ = map read (words line) in (x, y, z)
    let points = map readPoint linesOfContents
    return points


writePoints :: FilePath -> [Point] -> IO ()
writePoints filename points = writeFile filename (unlines (map show points))

quicksort :: [Point] -> [Point]
quicksort [] = []
quicksort (p:ps) = 
    let smallerSorted = quicksort [a | a <- ps, distance a <= distance p]
        biggerSorted = quicksort [a | a <- ps, distance a > distance p]
    in smallerSorted ++ [p] ++ biggerSorted
    
main :: IO ()
main = do
    start <- getCPUTime
    args <- getArgs
    let input_filename = args !! 0
    let output_filename = args !! 1
    points <- readPoints input_filename
    let sortedPoints = quicksort points
    writePoints output_filename sortedPoints
    end <- getCPUTime
    let diff = (fromIntegral (end - start)) / (10^12)
    appendFile "timings.txt" (show diff ++ "\n")
