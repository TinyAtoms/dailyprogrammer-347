#include <iostream>
#include <vector>
#include <cmath>

std::string print_vector(std::vector<int> myvector)
{
    std::string mystring;
    for (int i : myvector)
        mystring += std::to_string(i);
    mystring += "\n";
    return mystring;
}

int decompose_and_sum(int number)
{
    std::vector<int> number_repr;
    int digits = std::to_string(number).size() - 1;
    for (int i = digits; i >= 0; i--)
    {
        number_repr.push_back(number / std::pow(10, i));
        number -= (std::pow(10, i) * number_repr.back());
    }
    int sum = 0;
    for (int i : number_repr)
        sum += i;
    return sum;
}

int bonus_additive_persistence(int number)
{
    int count = 0;
    while (number >= 10)
    {
        int newnumber = decompose_and_sum(number);
        number = newnumber;
        count += 1;
    }
    return count;
}

int main()
{
    std::cout << bonus_additive_persistence(13);
    std::cout << bonus_additive_persistence(1234);
    std::cout << bonus_additive_persistence(9876);
    std::cout << bonus_additive_persistence(199);
}
