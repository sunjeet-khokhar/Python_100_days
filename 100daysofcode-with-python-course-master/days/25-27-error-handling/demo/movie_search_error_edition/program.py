import api
import requests.exceptions


def main():
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)
        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")
    except requests.exceptions.ConnectionError:
        print("ERROR: , could not connect to the API check whether you have juice?")
    except ValueError:
        print("You must enter a search term")
    except requests.exceptions.HTTPError:
        print("ERROR : You have entered an unacceptable search terms"
              "Please only enter alpha numeric characters")
    except Exception as e:
        #catch general exceptions
        print(type(e))
        print(f"An error has occured --> {e}")
    finally:
        print("THis will run no matter what !")

if __name__ == '__main__':
    main()

