import levels

class LevelSelector:
    levels = [None, levels.Level1, levels.Level2, levels.Level3, levels.Level4, levels.Level5, levels.Level6,
              levels.Level7, levels.Level8, levels.Level9, levels.Level10, levels.Level11, levels.Level12,
              levels.Level13, levels.Level14, levels.Level15, levels.Level16, levels.Level17, levels.Level18,
              levels.Level19, levels.Level20, levels.Level21, levels.Level22, levels.Level23, levels.Level24,
              levels.Level25,levels]  

    @staticmethod
    def select_level():
        print("Choose a level to play:")
        for i in range(1, len(LevelSelector.levels)):
            print(f"{i}. Level {i}")
        choice = input("Enter the number of the level: ")

        try:
            choice_num = int(choice)
            if 1 <= choice_num < len(LevelSelector.levels):
                level = LevelSelector.levels[choice_num]()
                level.display()
            else:
                print("Invalid choice. Please select a valid level.")
                LevelSelector.select_level()  
        except ValueError:
            print("Invalid input. Please enter a number.")
            LevelSelector.select_level()  
