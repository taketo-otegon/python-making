import random

class JankenSimulator:
    def __init__(self):
        self.human_choice = None
        self.human_index = None
        self.computer_choice = None
        self.computer_index = None
        self.options = ['グー', 'チョキ', 'パー']
        self.result_table = [[0,1,-1],
                            [-1,0,1],
                            [1,-1,0]]
    
    def get_index_choice(self,choice): #インデックスを取得する関数
        for index,element in enumerate(self.options):
            if choice == element:
                return index

    def get_computer_choice(self):
        choice = random.choice(self.options)
        index = self.get_index_choice(choice)
        return index,choice
    
    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(self.options,1)))

    def get_human_choice(self):

        choice_number = int(input('か'.join([f'「{option}」' for option in self.options])+"を番号で選んでください:")) - 1
        return choice_number,self.options[choice_number]
    

    def print_decision(self,name,choice):
        print(f'{name}が選んだのは「{choice}」です。')

    def print_choices(self):
        self.print_decision('あなた',self.human_choice)
        self.print_decision('コンピュータ',self.computer_choice)
    
    def get_result(self):
        return self.result_table[self.human_index][self.computer_index]

    def print_result(self):
        result = self.get_result()

        if result == 1:
            print(f'おめでとうございます! {self.human_choice}の勝ちです。')
        elif result == -1:
            print(f'残念でした。{self.computer_choice}の勝ちです。')
        else:
            print('引き分けです。')
        return
    
    def run(self):
        self.print_options()
        self.human_index,self.human_choice = self.get_human_choice()
        self.computer_index,self.computer_choice = self.get_computer_choice()
        self.print_choices()
        self.print_result()
    
if __name__ == '__main__':
    simulator = JankenSimulator()
    simulator.run()
