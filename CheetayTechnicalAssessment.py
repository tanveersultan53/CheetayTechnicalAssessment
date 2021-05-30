#Muhammad Tanveer Sultan (Python Developer)

#activity selection task
def ActivitySelection(start, finish, n):
  print("The following activities are selected:")
  j = 0
  print(j,end=" ")
  for i in range(1,n):
        if start[i] >= finish[j]:
          print(i,end=" ")
          j = i
#find equilibrium Point task
def equilibriumPoint(arr,n):
  sum_of_all_element = 0
  remaining_sum=0;
  for item in arr:
    sum_of_all_element+=item
  for i in range(n):
    sum_of_all_element-=arr[i]
    if sum_of_all_element==remaining_sum:
      return '{} equilibrium point is at position {}'.format(arr[i],i)
    remaining_sum+=arr[i]
  return '-1'

#find longest sub_string ditinct character
def longestSubstrDitinctChars(s):
    longest, start, visited = 0, 0, [False for _ in range(256)]
    for i, char in enumerate(s):
        if visited[ord(char)]:
            while char != s[start]:
                visited[ord(s[start])] = False
                start += 1
            start += 1
        else:
            visited[ord(char)] = True
        longest = max(longest, i - start + 1)
    return longest

#find maximum held meeting task
class MaximumMeeting:
    def __init__(self, startMeeting, endMeeting, position):
        self.startMeeting = startMeeting
        self.endMeeting = endMeeting
        self.position = position
def maximumMeetings(meeting, n):
    ans = []
    count = 1
    # Sorting of meetings
    meeting.sort(key=lambda x: x.endMeeting)
    # First meeting is selected
    ans.append(meeting[0].position)
    prev_end = meeting[0].endMeeting
    # Checking  meeting can take place or not
    for i in range(1, n):
        if meeting[i].startMeeting > prev_end:
            ans.append(meeting[i].position)
            prev_end = meeting[i].endMeeting
            count = count + 1

    print("Total Meeting Take Can Place:", count)