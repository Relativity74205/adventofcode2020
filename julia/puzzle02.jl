import DataStructures

raw_data = readlines("data/puzzle02.txt")


function check_password_entry_a(entry::String)::Bool
    policy, password = split(entry, ": ")
    policy_char_range_string, policy_char = split(policy, ' ')
    policy_char_range_arr = collect(parse(Int, ele) for ele in split(policy_char_range_string, "-"))
    policy_char_range = UnitRange(policy_char_range_arr[1], policy_char_range_arr[2])
    return DataStructures.counter(password)[policy_char[1]] in policy_char_range
end


function check_password_entry_b(entry::String)::Bool
    policy, password = split(entry, ": ")
    policy_char_range_string, policy_char = split(policy, ' ')
    policy_char_range = collect(parse(Int, ele) for ele in split(policy_char_range_string, "-"))
    return (password[policy_char_range[1]] == policy_char[1]) != (password[policy_char_range[2]] == policy_char[1])
end

println("Result for A is $(sum(check_password_entry_a(ele) for ele in raw_data))")
println("Result for B is $(sum(check_password_entry_b(ele) for ele in raw_data))")
