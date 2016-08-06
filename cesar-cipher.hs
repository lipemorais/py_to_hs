-- Cesar-Cipher
import Data.Char

encode :: Int -> String -> String
encode shift msg =
    let ords = map ord msg
        shifted = map (+ shift) ords
    in  map chr shifted

encode' :: Int -> String -> String
encode' shift msg = map (chr . (+ shift) . ord) msg

decode :: Int -> String -> String
decode shift msg =
    let ords = map ord msg
        shifted = map (+(negate shift)) ords
    in  map chr shifted

decode'  :: Int -> String -> String
decode'  shift msg = map (chr . (+(negate shift)) . ord) msg

decode'' :: Int -> String -> String
decode'' shift msg = encode (negate shift) msg

-- Python
-- chr(ord('a')+3)
