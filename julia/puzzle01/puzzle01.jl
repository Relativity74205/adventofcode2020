import IterTools

raw_data = readlines("julia/puzzle01/puzzle01.txt")
data = [parse(Int, ele) for ele in raw_data]

function solve(target_number, all_numbers, amount_numbers)
    combinations = IterTools.subsets(all_numbers, amount_numbers)
    for numbers in combinations
        if sum(numbers) == target_number
            return reduce(*, numbers)
        end
    end
end

println("Solution to Part A is $(solve(2020, data, 2))")
println("Solution to Part B is $(solve(2020, data, 3))")
