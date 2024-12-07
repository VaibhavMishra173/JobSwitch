#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

using namespace std;

// int main()
// {
//     int x, remainder, reverse = 0;
//     cin >> x;
//     int y=x;
//     while (x != 0)
//     {
//         remainder = x % 10;
//         reverse = reverse * 10 + remainder;
//         x /= 10;
//     }
//     cout << reverse<<y;
//     if (reverse == y)
//     cout<<4444;
//     return 0;
// }
// int y, remainder, reverse = 0;
// y = x;
// if (x < 0)
// {
//     return false;
// }
// else
// {
//     while (x != 0)
//     {
//         remainder = x % 10;
//         reverse = reverse * 10 + remainder;
//         x /= 10;
//     }
//     if (reverse == y)
//     {
//         return true;
//     }
//     else{
//         return false;
//     }
// }

// if (x < 0 || (x % 10 == 0 && x != 0))
// {
//     return false;
// }

// int rev = 0;
// while (x > rev)
// {
//     rev = rev * 10 + x % 10;
//     x /= 10;
// }
// return x == rev || x == rev / 10;
