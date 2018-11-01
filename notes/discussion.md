# Task 4

## General Considerations

year, gender, rank: all have known shapes
name does not

### Columns vs. Rows
- fewer columns, more rows
- easier to add rows to traditional DBs

len(year) >> len(gender)
len(year) >> len(rank)



### Multi-Index DF
columns: gender > rank
row index: year
cells: name

### No index
columns: year, gender, rank, name
row index: N/A

### Combine gender and rank
columns: F1 -> M5
row index: year
cells: name






1. Search by "Emma" and Rank 1

name
    gender
    years_ranked_1 [year]
    years_ranked_2 [year]
    years_ranked_3 [year]
    years_ranked_4 [year]
    years_ranked_5 [year]


2. Search by Rank 1 and gender (don't need year)

rank
    gender
        name [list w/o year]


name
    gender
    rank_in_year [year: rank]

year
    gender
        rank_1 [name]
        rank_2 [name]
        rank_3 [name]
        rank_4 [name]
        rank_5 [name]

3. Search by gender then year
gender
    year
        name [list w/o rank]

4. Search by gender
gender
    name [list w/o year or rank]

5. Search by gender
gender
    rank
        year
            name
