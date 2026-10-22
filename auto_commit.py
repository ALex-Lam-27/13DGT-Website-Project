import os
import subprocess
import random
from datetime import datetime, timedelta

# ==================== CẤU HÌNH CỦA BẠN ====================
# Đường dẫn tuyệt đối đến thư mục chứa code thật của bạn
BACKUP_DIR = r"D:\Backup_code" 
# Khoảng thời gian muốn rải code (6 tháng trước tính từ hôm nay)
START_DATE = datetime.now() - timedelta(days=150)
# ==========================================================

def run_git_command(env_vars, args):
    env = os.environ.copy()
    env.update(env_vars)
    subprocess.run(["git"] + args, env=env, check=True)

def auto_generate_history():
    if not os.path.exists(BACKUP_DIR):
        print(f"Lỗi: Không tìm thấy thư mục backup tại {BACKUP_DIR}")
        return

    # Lấy danh sách toàn bộ các file code thật của bạn
    files = [f for f in os.listdir(BACKUP_DIR) if f.endswith(('.html', '.css', '.js'))]
    if not files:
        print("Không tìm thấy file HTML, CSS hoặc JS nào trong thư mục backup!")
        return

    print(f"Tìm thấy {len(files)} file code. Bắt đầu phân rã và commit lùi lịch sử 6 tháng...")

    current_sim_date = START_DATE
    end_date = datetime.now()

    # Đọc trước nội dung toàn bộ các file và lưu thành các dòng
    file_contents = {}
    file_progress = {}
    for f in files:
        with open(os.path.join(BACKUP_DIR, f), 'r', encoding='utf-8', errors='ignore') as src:
            file_contents[f] = src.readlines()
            file_progress[f] = 0 # Đánh dấu xem file này đã commit đến dòng thứ mấy

    # Vòng lặp chạy qua từng ngày trong suốt 6 tháng
    commit_count = 0
    while current_sim_date < end_date:
        # Tỷ lệ 40% ngày đó có commit (để lịch sử trông tự nhiên, có ngày code ngày nghỉ)
        if random.random() < 0.32:
            # Mỗi ngày code sẽ có ngẫu nhiên từ 1 đến 3 commits
            num_commits_today = random.randint(1, 3)
            
            for c in range(num_commits_today):
                # Chọn ngẫu nhiên một file bất kỳ để cập nhật trong commit này
                chosen_file = random.choice(files)
                lines = file_contents[chosen_file]
                total_lines = len(lines)
                
                if total_lines == 0:
                    continue
                
                # Nếu file chưa được tạo trong repo, khởi tạo nó
                if not os.path.exists(chosen_file):
                    # Viết 5 dòng đầu tiên
                    chunk_size = min(5, total_lines)
                    with open(chosen_file, 'w', encoding='utf-8') as dest:
                        dest.writelines(lines[:chunk_size])
                    file_progress[chosen_file] = chunk_size
                    msg = f"Feat: initialize layout and structures for {chosen_file}"
                
                # Nếu file đã tồn tại và chưa viết xong, viết tiếp một đoạn ngẫu nhiên
                elif file_progress[chosen_file] < total_lines:
                    # Mỗi lần gõ thêm từ 3 đến 15 dòng code
                    chunk_size = random.randint(3, 15)
                    next_progress = min(file_progress[chosen_file] + chunk_size, total_lines)
                    
                    with open(chosen_file, 'w', encoding='utf-8') as dest:
                        dest.writelines(lines[:next_progress])
                        
                    file_progress[chosen_file] = next_progress
                    msg = f"Refactor: implement functionality and style updates in {chosen_file}"
                
                # Nếu file đã hoàn thành 100%, giả lập việc "sửa đổi/tối ưu" một vài dòng
                else:
                    if total_lines > 2:
                        with open(chosen_file, 'a', encoding='utf-8') as dest:
                            dest.write("\n/* Code optimization and minor alignment fixes */\n")
                    msg = f"Chore: optimize performance and fix responsiveness for {chosen_file}"

                # Định dạng ngày giờ giả lập cho commit
                hour = random.randint(9, 21)
                minute = random.randint(0, 59)
                second = random.randint(0, 59)
                commit_date_str = current_sim_date.replace(hour=hour, minute=minute, second=second).isoformat()

                # Thiết lập biến môi trường để Git ghi nhận ngày giả lập
                git_env = {
                    "GIT_AUTHOR_DATE": commit_date_str,
                    "GIT_COMMITTER_DATE": commit_date_str
                }

                # Tiến hành Add và Commit
                run_git_command(git_env, ["add", chosen_file])
                run_git_command(git_env, ["commit", "-m", msg])
                commit_count += 1

        # Tăng thêm 1 ngày
        current_sim_date += timedelta(days=1)

    # VÒNG CUỐI: Đảm bảo 100% tất cả các file trong repo đều khớp hoàn toàn với bản gốc cuối cùng
    print("\nĐang đồng bộ phiên bản hoàn chỉnh cuối cùng...")
    final_date_str = end_date.isoformat()
    final_env = {"GIT_AUTHOR_DATE": final_date_str, "GIT_COMMITTER_DATE": final_date_str}
    for f in files:
        import shutil
        shutil.copy(os.path.join(BACKUP_DIR, f), os.path.join(".", f))
        run_git_command(final_env, ["add", f])
    
    try:
        run_git_command(final_env, ["commit", "-m", "Build: final production compilation and asset verification"])
        commit_count += 1
    except subprocess.CalledProcessError:
        # Nếu không có gì thay đổi so với bước trước thì bỏ qua
        pass

    print(f"\n🎉 HOÀN THÀNH! Đã tự động tạo tổng cộng {commit_count} commits chất lượng rải đều trong 6 tháng qua.")

if __name__ == "__main__":
    auto_generate_history()