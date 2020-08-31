import csv, itertools, json

def main():
    with open("PrintYourOwnAdventureGame.csv", "r") as f:
        reader = csv.DictReader(f, fieldnames=("game", "game_stage", "games_stage_tail_text", "yellow_button", "blue_button", "reset_button")) 
        next(reader, None) # skipping those darn headers
        csv_data = list(reader)

        games_list = []
        game_stages_list = []

        # Grouping by game
        for k, g in itertools.groupby(csv_data, key=lambda r: (r["game"])):
            game_num = int(k)        

            # For each game, create a list of dictionary of game stage dict objs that
            # contains the game stage id, the game stage text and its buttons text
            for e in g:
                if int(e["game"]) == game_num:
                    game_stages_list.append({
                        "id" : int(e["game_stage"]),
                        "text" : e["games_stage_tail_text"],
                        "button" : (e["yellow_button"], e["blue_button"], e["reset_button"])
                    })
            
            # Add this list of game_stages dicts to the games list
            games_list.append({
                "game":int(k),
                "game_stage":game_stages_list,
            })

            # This is the clean the game stages list before populating it 
            # for the next game data
            game_stages_list = []

    # Create JSON file
    output_json = json.dumps(games_list)

    return output_json

def write_to_file(output_json):
    with open("result.json", "w") as wf:
        wf.write(output_json)

if __name__ == "__main__":
    main()





