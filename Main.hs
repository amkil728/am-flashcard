{-# OPTIONS_GHC -Wno-unrecognised-pragmas #-}
{-# HLINT ignore "Use <&>" #-}
{-# HLINT ignore "Redundant <$>" #-}
module Main where

import Flashcard
import Data.Functor ((<&>))

main :: IO ()
main = do
    deck <- readDeck "cards.txt"
    res <- mainLoop deck
    print res
    return ()

-- given a deck of cards
-- display each card to the user
-- accept feedback - did the user get it right?
-- if yes, remove it to a second deck
-- if no, keep it
-- return two decks, containing cards which need to be practiced, and
-- cards which are done
runDeck :: Deck -> IO (Deck, Deck)
runDeck deck = go deck ([], []) where
    go [] decks = return decks
    go (c@(Card f b):d) (d1, d2) =
        do
            putStr f
            getChar
            putStrLn b
            answer <- getLine
            if answer == "y" then go d (d1, c:d2)
                else go d (c:d1, d2)


mainLoop :: Deck -> IO (Deck, Deck)
mainLoop deck = runDeck deck >>=
    \(d1, d2) -> case d1 of
        [] -> return ([], d2)
        _  -> do
            putStrLn "Continue?"
            continue <- getLine
            if continue == "y" then
                do result <- mainLoop d1
                   let (d1', d2') = result
                   return (d1', d2' ++ d2)
            else return (d1, d2)


alternateLines :: [String] -> ([String], [String])
alternateLines [] = ([], [])
alternateLines [l] = ([l], [])
alternateLines (l1:l2:ls) = (l1:l1s, l2:l2s) where
    (l1s, l2s) = alternateLines ls


readDeck :: FilePath -> IO Deck
-- readCards path = return (zipWith Card fronts backs)
--     where
--         fronts :: [String]
--         backs :: [String]
--         (fronts, backs) = 
readDeck path = do
    s <- readFile path
    let (fronts, backs) = alternateLines (lines s)
    return (zipWith Card fronts backs)


writeDeck :: Deck -> FilePath -> IO ()
writeDeck = undefined