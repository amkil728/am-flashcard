module Flashcard where

data Card = Card {front :: String, back :: String}
    deriving (Eq, Show)

type Deck = [Card]

addCard :: Card -> Deck -> Deck
addCard = (:)

getCard :: Int -> Deck -> Card
getCard i = (!! i)

removeCard :: Int -> Deck -> (Card, Deck)
removeCard i d = (head back, front ++ back) where
    (front, back) = splitAt i d

-- not checking index bounds
moveCard :: Int -> (Deck, Deck) -> (Deck, Deck)
moveCard i (d1, d2) = (d, addCard c d2) where
    (c, d) = removeCard i d1

displayCard :: Card -> IO ()
displayCard (Card f b) = do
    putStrLn f
    putStrLn b