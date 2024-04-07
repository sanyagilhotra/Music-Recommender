import gradio as gr
import recommender_script

def get_recommendations(artist, song, lyrics, rec_num):
    list_of_recs = recommender_script.get_selection(artist, song, lyrics, rec_num)
    recommendations=""
    for i in list_of_recs:
        recommendations += f"\n{i[0]} by {(i[1][1])}\n"
    return recommendations

with gr.Blocks() as demo:
    gr.Markdown("# Song Recommender")
    with gr.Row():
        artist = gr.Textbox(label="Artist Name")
        song = gr.Textbox(label="Song Title")
    lyrics = gr.Textbox(label="Song Lyrics", lines=5)
    rec_num = gr.Slider(label="Number of Recommendations", minimum=1, maximum=50, value=5, step=1)
    output = gr.Textbox(label="Recommended Songs")
    btn = gr.Button("Get Recommendations")
    btn.click(get_recommendations, inputs=[artist, song, lyrics, rec_num], outputs=output)

demo.launch()