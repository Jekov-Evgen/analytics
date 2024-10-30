from pytube import YouTube


def getting_data_from_links(list_of_links : list[str]):
    result = []
    
    for i in range(len(list_of_links)):
        yt = YouTube(list_of_links[i])
        temp = []
        go_to_res = []
        temp.append(yt.title)
        temp.append(yt.views)
        
        go_to_res.append(temp)
        result.append(go_to_res)
        
    print(result)
    
    
print(getting_data_from_links(['https://www.youtube.com/watch?v=UPLg6u4bE-M', 'https://www.youtube.com/watch?v=UPLg6u4bE-M']))