import heuristics
import match


if __name__ == "__main__":
    #match.player_vs_player()
    #match.player_vs_pc(heuristics.piece_count, 1)
    #match.pc_vs_pc(heuristics.control_center, heuristics.control_edge)
    match.pc_vs_pc(heuristics.piece_count, heuristics.control_edge,True,False)
