sayMe :: (Integral a) => a -> String  
sayMe 1 = "One!"  
sayMe 2 = "Two!"  
sayMe 3 = "Three!"  
sayMe 4 = "Four!"  
sayMe 5 = "Five!"  
sayMe x = "Not between 1 and 5"  

-- not defining then everything is fine.
-- can we not doing this?
-- main = print "this is main lazero program."
-- what i see is a huge waste in storage space and computation.
-- the space shall be unified, while computation should be non-deterministic.
main = print $ sayMe 5