def main():
  grid = int(input("Enter the volume of the grid: "))
  rows = int(input("Enter the number of rows: "))
  cols = int(input("Enter the number of columns: "))

  grid = create_grid(rows, cols)

  print("\nInitial Grid:")
  print_grid(grid)

  while True:
    coords = input("\nEnter the cell coordinate to edit: ")

    if coords == "done":
      break

    try:
      row, col = map(int, coords.split(","))
      if 0 <= row < rows and 0 <= col < cols:
        new_value = input("Enter new value for the cell: ")
        grid[row][col] = new_value

        print("\nUpdated Grid:")
        print_grid(grid)
      else:
        print("Invalid coordinates.")
    except ValueError:
      print("Invalid input.")

if __name__ == "__main__":
  main()
