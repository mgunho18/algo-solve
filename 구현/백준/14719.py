# h, w = map(int, input().split())
# heights = list(map(int, input().split()))
# ans = 0
#
#
# def cal_water_amt(heights):
#     global ans
#
#     if sum(heights) == 0:
#         return
#
#     for i in range(len(heights)):
#         if heights[i] != 0:
#             start_idx = i
#             break
#
#     prev = heights[start_idx]
#     blocks = [prev]
#     for each in heights[start_idx + 1:]:
#         if each < prev:
#             blocks.append(each)
#         else:
#             ans += len(blocks) * prev - sum(blocks)
#             prev = each
#             blocks = [each]
#
#     if len(blocks) >= 3:
#         blocks.reverse()
#         cal_water_amt(blocks)
#
#
# cal_water_amt(heights)
# print(ans)

h, w = map(int, input().split())
heights = list(map(int, input().split()))
ans = 0

max_val = 0
max_idx = 0
for i in range(w):
    if heights[i] > max_val:
        max_val = heights[i]
        max_idx = i

tmp_max = 0
for idx in range(max_idx + 1):
    tmp_max = max(tmp_max, heights[idx])
    ans += tmp_max

tmp_max = 0
for idx in range(w - 1, max_idx, -1):
    tmp_max = max(tmp_max, heights[idx])
    ans += tmp_max

print(ans - sum(heights))
