class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c: set() for w in words for c in w}
        indegree={c:0 for c in adj}
    
        res=""
      
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            
            minLen=min(len(w1), len(w2))

            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j]!=w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1

                    break
  

        
        q=deque()
        for n in indegree:
            if indegree[n]==0:
                q.append(n)
        print(q)
        while q:
            node=q.popleft()
            res+=node
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    q.append(nei)
        return res if len(res)==len(indegree) else ""

        
