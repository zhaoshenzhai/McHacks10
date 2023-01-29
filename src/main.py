import scrape
import sentiment
import plot

cont = True
while cont:
    option = input("Welcome!\nPlease choose among the following options:\n"
                   "\t1. Evaluate the “vibe” for one post\n"
                   "\t2. Evaluate the “vibe” of several posts from a subreddit\n"
                   "\nYour option (1 or 2): ")
    if option == "1":
        url = input("Please enter the url of the post: ")
        vibe, cpds = sentiment.vibe_per_post(url)
        plot.gen_pie(vibe)
        plot.gen_hist(cpds)
        
    elif option == "2":
        name = input("Please enter the name of the subreddit: ")
        vibe = sentiment.vibe_per_subreddit(scrape.get_links(name))
        plot.gen_pie(vibe)
        
    else:
        print("Invalid input!!")
        break
    
    is_cont = input("Please enter 'C' to evaluate another post / subreddit: ")
    if is_cont == "C":
        cont = True
        print("\033c", end='')
    else:
        cont = False
