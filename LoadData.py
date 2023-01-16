from river import stream
import pandas as pd
def streaming():
    df = pd.read_csv("amazon_bis.txt", sep="\t", on_bad_lines='skip')
    df_stream = stream.iter_pandas(df)
    corespondance = dict()
    j = 0
    for w in df_stream:

        if w[0]['FromNodeId'] in corespondance.keys():
            pass
        else:
            corespondance[str(w[0]['FromNodeId'])] = j
            j += 1
        if w[0]['ToNodeId'] in corespondance.keys():
            pass
        else:
            corespondance[str(w[0]['ToNodeId'])] = j
            j += 1

        yield [corespondance[str(w[0]['FromNodeId'])], corespondance[str(w[0]['ToNodeId'])]]
