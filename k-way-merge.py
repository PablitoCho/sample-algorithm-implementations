# https://www.baeldung.com/cs/2-way-vs-k-way-merge

def merge_sort(seq):
  if len(seq) < 2:
    return seq
  mid = len(seq) // 2
  left, right = seq[:mid], seq[mid:]
  if len(left) > 1:
    left = merge_sort(left)
  if len(right) > 1:
    right = merge_sort(right)  
  result = []
  print(f'left {left} vs right {right}')
  while left and right:
    print(f"compare {left[-1]} vs {right[-1]}")
    if left[-1] >= right[-1]:
      result.append(left.pop())
    else:
      result.append(right.pop())
  result.reverse()
  return (left or right) + result

def k_way_merge(*lists):
  # print(f"input {lists}")
  result = []
  # cnt = 1
  flattened = [el for ls in lists for el in ls]
  while flattened:
    # print(f"{cnt} loop ===============")
    aux = {}
    for i, ls in enumerate(lists):
      # print(ls)
      if ls:
        aux[i] = ls[0]
    # print(f"aux {aux}")
    sorted = merge_sort(list(aux.values()))
    # print(f"sorted {sorted}")
    val = sorted[0]
    result.append(val)
    lists[list(aux.keys())[list(aux.values()).index(val)]].pop(0)
    flattened = [el for ls in lists for el in ls]
    # cnt += 1
  return result

def read_segment(path):
  ls = []
  with open(path, "r") as file:
    for line in file:
      ls.append((line.split(',')[0], ''.join(line.split(',')[1:]).strip()))
  return ls

def k_way_merge_segments(*segments_paths):
  import heapq
  # heap을 사용하는 이유
  # https://medium.com/@amitrajit_bose/merge-k-sorted-arrays-6f9427661e67
  # [[('key2', 'value2'), ('key5', 'value5'), ('key10', 'value10'), ('key17', 'value17')], 
  #  [('key4', 'value4'), ('key6', 'value6'), ('key8', 'value8')], 
  #  [('key3', 'value3'), ('key7', 'value7')], 
  #  [('key1', 'value1'), ('key15', 'value15'), ('key20', 'value20')]]
  
  # paths를 역순으로 index 생성 필요 (최소 heap 이용)
  segments_paths_list = list(segments_paths)
  segments_paths_list.sort(reverse=True)

  heap = []
  for segment_index, segment_path in enumerate(segments_paths_list):
    segment_data = read_segment(segment_path)
    for key, value in segment_data:
      heap.append((key, segment_index, value))
  # 최소 heap 구성
  heapq.heapify(heap)

  result = []
  previous_key = None
  while heap:
      key, segment_index, value = heapq.heappop(heap)
      print(f"popped key {key}, segment_file {segments_paths_list[segment_index]}")
      if previous_key == key: # if previously added skip
        continue
      result.append((key, value))
      previous_key = key
  return result


def merge1(*lists):
    # https://medium.com/@amitrajit_bose/merge-k-sorted-arrays-6f9427661e67
    import heapq
    result = []
    heap = [(ls[0], i, 0) for i, ls in enumerate(lists) if ls]
    heapq.heapify(heap)

    while heap:
        print(f"heap {heap}")
        val, list_index, element_index = heapq.heappop(heap)
        print(f"poped val {val}, list_index {list_index}, element_index {element_index}")
        result.append(val)
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1],
                          list_index,
                          element_index + 1)
            heapq.heappush(heap, next_tuple)
    return result



if __name__ == '__main__':
  # l1, l2, l3, l4 = [2, 5, 10, 17], [4, 6, 8], [3, 5, 7], [1, 15, 20]
  # result = merge1(l1, l2, l3, l4)
  # print(result)
  # result = k_way_merge(l1, l2, l3, l4)
  # print(result)
  seg1, seg2, seg3, seg4 = 'data/segment1.dat', 'data/segment2.dat', 'data/segment3.dat', 'data/segment4.dat'
  merged = k_way_merge_segments(seg1, seg2, seg3, seg4)
  print(merged)

  # ls = [4, 6, 2, 8, 0, 5, 9, 7, 1, 3]
  # sorted = merge_sort(ls)
  # print(sorted)