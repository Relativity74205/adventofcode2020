import IterTools

data = Vector{String}[]
open("julia/puzzle01/puzzle01.txt") do f
    for line in readlines(f)
        append!(data, line)
    end
end
data = [parse(Int, ele) for ele in data]

function solve(target_number, all_numbers, amount_numbers)
    for numbers in IterTools.subsets(all_numbers, amount_numbers)
        if sum(numbers) == target_number
            return reduce(*, numbers)
        end
    end
end

println("Solution to Part A is $(solve(2020, data, 2))")
println("Solution to Part B is $(solve(2020, data, 3))")
