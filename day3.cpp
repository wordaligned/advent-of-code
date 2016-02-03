#include <cstdio>
#include <iostream>
#include <set>
#include <utility>

int main() {
    int x = 0, y = 0;
    std::set<std::pair<int, int>> visited = {{x, y}};
        
    for (char c; std::cin.get(c);) {
        switch (c) {
        case '>': ++x; break;
        case '<': --x; break;
        case '^': ++y; break;
        case 'v': --y; break;
        default:
            std::cerr << "Unexpected char: " << c << '\n';
            std::exit(1);
        }
        visited.insert({x, y});
    }
    std::cout << visited.size() << '\n';
    std::exit(0);
}
