# 리스트를 반으로 나누어 정렬되지 않은 리스트를 만든다.
# 정렬되지 않은 두 리스트의 크기가 1이 될때까지, 계속 리스트를 반으로 나누어 병합 정렬 알고리즘을 재귀 호출
# 안정적이고, 대규모 데이터에 대해 속도가 빠르다 -> O(n logn)

# 데이터가 너무 커서 메모리에 넣지 못 할때, 병합 정렬은 좋은 선택
# 하위 데이터 집합은 메모리에서 정렬할 수 있을 만큼 작아질때까지 별도 파일로 디스크에 저장할 수 있기 때문.

# 병합 방식 : 각 파일에서 한 번에 하나의 요소를 읽고, 순서대로 최종 파일에 기록

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
  while left and right:
    if left[-1] >= right[-1]:
      result.append(left.pop())
    else:
      result.append(right.pop())
  result.reverse()
  return (left or right) + result

def merge_sort_sep(seq):
  # 두 함수로 나누어 구현. 한 함수에서는 배열을 나누고, 나머지 함수에서는 배열을 병합
  if len(seq) < 2:
    return seq
  mid = len(seq) // 2
  left  = merge_sort_sep(seq[:mid])
  right = merge_sort_sep(seq[mid:])
  return merge(left, right)

def merge(left, right):
  if not left or not right:
    return left or right
  result = []
  i, j = 0, 0
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  
  if left[i:]:
    result.extend(left[i:])
  if right[j:]:
    result.extend(right[j:])
  # print(result)
  return result

def merge_2n(left, right):
  # 이미 정렬된 상태. 시간 복잡도 O(n)
  if not left or not right:
    return left or right
  result = []
  while left and right:
    if left[-1] >= right[-1]:
      result.append(left.pop())
    else:
      result.append(right.pop())
  result.reverse()
  return (left or right) + result

def merge_files(filenames):
  result, final = [], []
  for filename in filenames:
    aux = []
    with open(filename, "r") as file:
      for line in file:
        aux.append(int(line))
    print(f'aux with file {filename} : {aux}')
    result.append(aux)
  print(f'result : {result}')
  final.extend(result.pop())
  for l in result:
    final = merge_2n(l, final)
  return final

if __name__ == '__main__':
  l1, l2 = [4, 6, 2, 8, 0], [5, 9, 7, 1, 3]
  l3 = l1 + l2
  result = merge_sort(l3)
  result_sep = merge_sort_sep(l3)
  print(result)
  print(result_sep)

  l4, l5 = [1,2,3,4,5,6,7], [2,4,5,8]
  result2n = merge_2n(l4, l5)
  print(result2n)

  filenames = ['data/a.dat', 'data/b.dat', 'data/c.dat']
  result_files = merge_files(filenames)
  print(result_files)