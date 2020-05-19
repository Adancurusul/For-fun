from lupa import *
lua = LuaRuntime()
lua_code = """
function(size)
    first = {}
    second = {}
    start_time = os.clock()
    for i = 0,size-1 do
        first[i]=math.random(size)
    end
    for i = 0 ,size-1 do
        second[i]=math.random(size)
    end
    print("LUA init time:" ..(os.clock()-start_time))
    start_time = os.clock()
    for i = 0 ,size-1 do
        if first[i]~=second[i] then
            first[i] = first[i]+second[i]
        end
    end
    
    print("LUA sum time :" ..(os.clock()-start_time))
end
"""

test = lua.eval(lua_code)
size = 5000000
test(size)
print("finish")