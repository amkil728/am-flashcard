alternateLines :: [String] -> ([String], [String])
alternateLines [] = ([], [])
alternateLines [l] = ([l], [])
alternateLines (l1:l2:ls) = (l1:l1s, l2:l2s) where
    (l1s, l2s) = alternateLines ls