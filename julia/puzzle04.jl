raw_data = readlines("data/puzzle04.txt")


data = []
passport = []
for line::String in raw_data
    if line == ""
        append!(data, passport)
        passport = []
    else
        append!(passport, line)
    end
end


##
for line in raw_data
    println(line)
end
