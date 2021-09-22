#include <bits/stdc++.h>

using namespace std;

const int maxn = 100005;

int n;
int a[maxn][2];
vector<int> g[maxn];
long long f[maxn][2];

void dfs_solve(int v, int p) {
    for(int s : g[v]) if (s != p) {
        dfs_solve(s, v);
        f[v][0] += max(f[s][0] + abs(a[s][0] - a[v][0]), f[s][1] + abs(a[s][1] - a[v][0]));
        f[v][1] += max(f[s][0] + abs(a[s][0] - a[v][1]), f[s][1] + abs(a[s][1] - a[v][1]));
    }
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int ntest; cin >> ntest;
    while(ntest--) {
        cin >> n;
        for(int i = 0; i < n; ++i) {
            cin >> a[i][0] >> a[i][1];
        }

        for(int i = 0; i + 1 < n; ++i) {
            int u, v; cin >> u >> v;
            --u; --v;
            g[u].push_back(v);
            g[v].push_back(u);
        }
            
        dfs_solve(0, -1);
        cout << max(f[0][0], f[0][1]) << endl;

        for(int i = 0; i < n; ++i) {
            g[i].clear();
            f[i][0] = f[i][1] = 0;
        }
    }
    return 0;
}
