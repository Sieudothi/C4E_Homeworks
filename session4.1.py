# create a movie in dictionary format
def create_movie(org_name, trans_name, year):
    return {
        "org_name": org_name,
        "trans_name": trans_name,
        "year": year
    }
#remove function
def remove_movie(m_list, movie):
    m_list.remove(movie)

# display a movie
def display_movie(m):
    print("Original name: ", m["org_name"])
    print("Translated name: ", m["trans_name"])
    print("Year: ", m["year"])
    print()

def display_movie_list(m_list):
     
    for i in range (len(m_list)):
        print("Movie# ", i+1)
        display_movie(m_list[i])

def search_movie_by_year(m_list, year):
    x = []
    for i in range(len(m_list)):
       if m_list[i]["year"] == year:
           x.append(m_list[i])
    return x

movie_list=[]
movie_list.append(create_movie("The hunger games", "Đấu trường sinh tử", 2016))
movie_list.append(create_movie("Break point", "Ranh giới chết", 2015))
movie_list.append(create_movie("Little Door Gods", "Tiểu Môn Thần", 2015))

movie_in_2015 = search_movie_by_year(movie_list, 2015)
display_movie_list(movie_in_2015)
