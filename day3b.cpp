#include <cstdio>
#include <functional>
#include <iostream>
#include <set>
#include <utility>

typedef std::pair<int, int> point;

point move(char c, int & x, int & y) {
    switch (c) {
    case '>': return {++x, y};
    case '<': return {--x, y};
    case '^': return {x, ++y};
    case 'v': return {x, --y};
    default:
        std::cerr << "Unexpected char: " << c << '\n';
        std::exit(1);
    }
}

int main() {
    int u = 0, v = 0;
    int x = 0, y = 0;

    std::set<point> visited = {{x, y}, {u, v}};

    std::function<point(char)> santas[] = {
        [&](char c) { return move(c, x, y); },
        [&](char c) { return move(c, u, v); }
    };

    int turn = 0;
    for (char c; std::cin.get(c); turn = !turn) {
        visited.insert(santas[turn](c));
    }
    std::cout << visited.size() << '\n';
    std::exit(0);
}
