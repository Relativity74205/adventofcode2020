raw_data = readlines("julia/puzzle05/puzzle05.txt")

const MAX_ROWS = 128
const MAX_COLS = 8
const COL_STEPS = Dict('L'=>-1, 'R'=>1)
const ROW_STEPS = Dict('F'=>-1, 'B'=>1)


function get_row(row_str::String)::Int
    region_length = MAX_ROWS
    steps = []
    for c in row_str
        append!(steps, region_length / 4 * (1 + ROW_STEPS[c]))
        region_length /= 2
    end

    return sum(steps)
end

function get_col(col_str::String)::Int
    region_width = MAX_COLS
    steps = []
    for c in col_str
        append!(steps, region_width / 4 * (1 + COL_STEPS[c]))
        region_width /= 2
    end

    return sum(steps)
end

function get_free_id(data::Vector{String})
    seats = Dict()

    for seat in data
        row = get_row(seat[1:7])
        col = get_col(seat[8:end])
        if !(row in keys(seats))
            seats[row] = []
        end
        append!(seats[row], col)
    end

    for (row, cols) in seats
        if length(cols) != 8 && row != minimum(keys(seats)) && row != maximum(keys(seats))
            free_col = pop!(setdiff(Set(0:7), Set(cols)))
            return row * 8 + free_col
        end
    end
end

free_id = get_free_id(raw_data)
seat_ids = [get_row(seat[1:7]) * 8 + get_col(seat[8:end]) for seat in raw_data]

println("Result for A is $(free_id).");
println("Result for B is $(maximum(seat_ids)).")
