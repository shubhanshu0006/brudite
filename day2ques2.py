#https://leetcode.com/problems/sort-characters-by-frequency/description/
class Solution {
public:
    string frequencySort(string s) {
        
           map<char,int>mp;
        for(int i=0;i<s.size();i++){
            mp[s[i]]++;
        }
        string ans="";
    vector<pair<int,char>>arr;
        for(auto i:mp){
            arr.push_back({i.second,i.first});
        }
        sort(arr.rbegin(),arr.rend());
        for(auto it:arr){
            int temp=it.first;
            while(temp--){
                ans+=it.second;
            }
        }
        return ans;
    }
};