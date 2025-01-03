 # Barra de progresso das notícias carregadas pela API


from tqdm import tqdm


def show_progress(iterable, description):
    return tqdm(iterable, desc=description, unit=" notícia")
