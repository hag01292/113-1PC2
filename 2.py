# 定義函式 gray
def gray(array, i, j, value):
    """
    更新稀疏矩陣的指定位置像素值。
    :param array: 用於儲存非零像素值的稀疏矩陣 (字典)
    :param i: 像素的行座標
    :param j: 像素的列座標
    :param value: 像素值
    """
    if value != 0:  # 僅儲存非零像素值
        array[(i, j)] = value

def print_sparse_matrix(array):
    """
    輸出稀疏矩陣中所有非零像素值及其位置。
    :param array: 儲存非零像素值的稀疏矩陣 (字典)
    """
    print("影像中非零像素值如下：")
    for position, value in array.items():
        print(f"像素位置 {position} = {value}")

# 主程式
if __name__ == "__main__":
    # 初始化稀疏矩陣
    sparse_matrix = {}

    # 呼叫 gray 函式儲存非零像素值
    gray(sparse_matrix, 0, 1, 50)
    gray(sparse_matrix, 1, 3, 120)
    gray(sparse_matrix, 2, 4, 180)
    gray(sparse_matrix, 3, 2, 255)

    # 快速印出所有非零像素值
    print_sparse_matrix(sparse_matrix)
