from redis_client import client

def normalizeCompletion(string):
    return string.lower().strip()

def insertCompletion(completion, score):
  completion = normalizeCompletion(completion)
  prefixes = []
  for i, c in enumerate(completion):
    prefixes.append(completion[:i+1])

  for prefix in prefixes:
    client.zadd(prefix, score, completion)
  
  return 'ok'

def searchPrefix(prefix):
  return client.zrange(prefix, 0, 5, desc=True, withscores=False)