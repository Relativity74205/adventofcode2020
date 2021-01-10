raw_data = readlines("data/puzzle03.txt")

function solve(data::Vector{String}, strategy::Tuple{Int, Int})::Int
    x, y = 1, 1
    height = length(data)
    width = length(data[1])

    amount_trees::Int = 0
    while 1 > 0
        if y > height
            return amount_trees
        end
        if x > width
            x -= width
        end

        amount_trees += data[y][x] == '#'
        x += strategy[1]
        y += strategy[2]
    end

end

result_a = solve(raw_data, (3, 1))
results_b = (solve(raw_data, strategy) for strategy in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)))

println("Result for A is $result_a")
println("Result for B is $(prod(results_b))")
