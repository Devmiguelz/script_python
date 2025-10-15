from bs4 import BeautifulSoup

def save_links_to_txt(links: list[str], filename: str, separator: str = "\n"):
    """
    Guarda los links en un archivo .txt
    :param links: lista de URLs
    :param filename: nombre del archivo .txt
    :param separator: "\n" para línea por línea, "|" para separados por |
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(separator.join(links))


html = """<div id="contents" class="style-scope ytd-rich-grid-renderer"><ytd-rich-item-renderer
        class="style-scope ytd-rich-grid-renderer" items-per-row="4" lockup="true" rendered-from-rich-grid=""
        is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/5czN4818mxU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/5czN4818mxU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAZXFdKDNbHmWt1nFzr8spxWiEmjg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/5czN4818mxU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que al cortar un aguacate mediano...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al cortar un aguacate mediano...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">34M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/VgvC-q8lLQ0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/VgvC-q8lLQ0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLATBoojuHKcDPvlKBhBe0_22-bYUA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/VgvC-q8lLQ0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="¡Receta fácil, rápida y deliciosa! 🍡🍡🍞"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Receta fácil, rápida y deliciosa! 🍡🍡🍞</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">31M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/3eRnWfWE9rI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/3eRnWfWE9rI/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCYKjeGsepUas6sxA-I4_eU-VjI_w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/3eRnWfWE9rI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Por qué no lo pensé antes! ¡Las fábricas de lámparas no quieren que lo sepas!"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Por qué no lo pensé antes! ¡Las fábricas de lámparas no quieren que
                                        lo sepas!</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">26M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/V-Plj_M5WoU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/V-Plj_M5WoU/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDPqEa0F-TODsCgc_WHSsFYTfnlow">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/V-Plj_M5WoU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Este secreto me lo enseño un carnicero ¡Y NO LE CREÍA! 😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Este secreto me lo enseño un carnicero ¡Y NO LE CREÍA! 😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">18M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/5qHjmPCuxag"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/5qHjmPCuxag/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAxwmWtbpNFowTLz-zzm3MMkZKxsg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/5qHjmPCuxag"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="La pizza más fácil del mundo, ¡Te Sorprenderá lo rica que queda!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">La pizza más fácil del mundo, ¡Te Sorprenderá lo rica que
                                        queda!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">17M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AkbUD9eQtXg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/AkbUD9eQtXg/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCdvsPdLF37IdemiE5voYsg88DTgA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AkbUD9eQtXg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí rallas 5 salchichas por...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí rallas 5 salchichas por...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">12M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/GsTR6m2lTw4"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/GsTR6m2lTw4/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCxgNk_ofUPD12DXcqxdzUWaG_10A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/GsTR6m2lTw4"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Mi abuela no aguantaba más el cansancio hasta que tomó esto, ella se renovó😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mi abuela no aguantaba más el cansancio hasta que tomó esto, ella se
                                        renovó😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">12M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/OPkznOa1iLU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/OPkznOa1iLU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBnVsjdixb2pA4aRoCqOdqDrdX29Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/OPkznOa1iLU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Esto hago cuando tengo visitas inesperadas en casa 🤭"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Esto hago cuando tengo visitas inesperadas en casa 🤭</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">11M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/xPIIfJAessM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/xPIIfJAessM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBtrGzBMfj1X2Pezc86fuAHhA8lPw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/xPIIfJAessM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que al colocar 3 tortillas...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al colocar 3 tortillas...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">10M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/5x3SJQ_lP3w"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/5x3SJQ_lP3w/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBK2xJZMtmnOrnuNwcIQhGTX2SWMg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/5x3SJQ_lP3w"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí rallas 2 plátanos por...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí rallas 2 plátanos por...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">10M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/s2_IToiZg_4"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/s2_IToiZg_4/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBNsmIbATBLCUs1lnwO0DNnOBWErg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/s2_IToiZg_4"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Sabías que sí agregas dos litros de leche en la cacerola...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas dos litros de leche en la
                                        cacerola...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">11M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/lODMQeh-Awg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/lODMQeh-Awg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAvCOf4v9kNrfXrrE_B8o_iXib0dg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/lODMQeh-Awg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Cuando hago papas fritas como estas, ¡todos me preguntan por la receta!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Cuando hago papas fritas como estas, ¡todos me preguntan por la
                                        receta!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">9.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/RvRKQqMjO-A"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/RvRKQqMjO-A/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDypbzpjMm0I7qbCW3D9Jn4mifd6w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/RvRKQqMjO-A"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí le agregas salsa de soya...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí le agregas salsa de soya...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">9.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/o61s0RNbp8w"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/o61s0RNbp8w/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCMfF2eShdMeBblwTim-095IgqD2g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/o61s0RNbp8w"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Descubre una forma deliciosa y fácil de hacer el desayuno😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Descubre una forma deliciosa y fácil de hacer el
                                        desayuno😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">9.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/lfKPjrTo2eU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/lfKPjrTo2eU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD0lkz1a_axJOuX6fHfRH0e04eU5w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/lfKPjrTo2eU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que al cortar finamente un brócoli mediano...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al cortar finamente un brócoli mediano...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">8.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/UxlVfw9VQGU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/UxlVfw9VQGU/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA-mF29A_B_y3QCJYDpGs3iVsolog">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/UxlVfw9VQGU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Vierte el huevo en la leche hirviendo ¡Ya no compro en el mercado!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Vierte el huevo en la leche hirviendo ¡Ya no compro en el
                                        mercado!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">8.2M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/wtFF0cCj9-I"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/wtFF0cCj9-I/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDVE-VZqy7T1algKkv1QR4WLzAXww">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/wtFF0cCj9-I"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Estos son los famosos huevos turcos de los que todo el mundo quiere saber la receta! 😋🤭🥚"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Estos son los famosos huevos turcos de los que todo el mundo quiere
                                        saber la receta! 😋🤭🥚</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">8.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/-Z6paGkAI40"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/-Z6paGkAI40/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBPALE5nHN7LF0Lp784X1LtnR5-yg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/-Z6paGkAI40"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí agregas costillas en el agua...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas costillas en el agua...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">7.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/s-9mgroPsm0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/s-9mgroPsm0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCryopbK6qd2Fvf-hyi34oy6ueG9g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/s-9mgroPsm0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Haz la lasaña en la sartén la próxima vez! ¡Es fácil, rápida y deliciosa!"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Haz la lasaña en la sartén la próxima vez! ¡Es fácil, rápida y
                                        deliciosa!</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">7.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/w__oz2OOABI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/w__oz2OOABI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDFyJV08ZBFYsEN1ubGtQcf3-RsrQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/w__oz2OOABI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Bolitas de queso, tan ricas que se derriten en la boca🧀" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Bolitas de queso, tan ricas que se derriten en la boca🧀</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">7.7M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PwazGYsZ6S0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PwazGYsZ6S0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB3oycm-9AV2l9g9Nj3emK81cUieA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PwazGYsZ6S0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Con este truco, cualquier sartén se volverá antiadherente.😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Con este truco, cualquier sartén se volverá
                                        antiadherente.😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">7.2M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/9dQtOSaO4AQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/9dQtOSaO4AQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCjh_B0jWXvkA3yjKfthlPNy91ENw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/9dQtOSaO4AQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Vierte el café en la leche condensada ¡Ya no compro en el mercado!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Vierte el café en la leche condensada ¡Ya no compro en el
                                        mercado!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">6.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/oFUEGQGzTsU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/oFUEGQGzTsU/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAt2nwOAz1owticRWMkMWEtwTSxKw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/oFUEGQGzTsU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Me preguntaron porque el pescado frito me quedo tan delicioso y crujiente ¡Mira el secreto!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Me preguntaron porque el pescado frito me quedo tan delicioso y
                                        crujiente ¡Mira el secreto!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">6.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/X77qFTy3zL8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/X77qFTy3zL8/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDOhjlivSGsSuwtOHPBIye33VMaPA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/X77qFTy3zL8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gusta el plátano es porque nunca te lo prepararon así. 🍌🍌"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gusta el plátano es porque nunca te lo prepararon así.
                                        🍌🍌</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/irggwbJ87bU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/irggwbJ87bU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAyYydORCgA7Hc1hu0Im55tsNbFMw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/irggwbJ87bU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Con esta receta fue con la que emprendí mi primer negocio😱😍  #arrozconleche #receta"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Con esta receta fue con la que emprendí mi primer negocio😱😍
                                        #arrozconleche #receta</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/XL4WzWUHALQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/XL4WzWUHALQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAvnHK8D6IP7xHxagiOCdZP_P1mxg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/XL4WzWUHALQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="No Comas Pan, Prepara esta deliciosa y saludable receta de desayuno😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">No Comas Pan, Prepara esta deliciosa y saludable receta de
                                        desayuno😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5.2M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/UTho3Ls_5DM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/UTho3Ls_5DM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAGG5BIPOZWeaLja-27L083eR_B1w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/UTho3Ls_5DM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Esta ensalada es tan saludable y nutritiva que la hago una y otra vez!"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Esta ensalada es tan saludable y nutritiva que la hago una y otra
                                        vez!</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/rJJHolt2-Lc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/rJJHolt2-Lc/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAnHjAj4TcqVQ2phoBfaYn_jP8kQA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/rJJHolt2-Lc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="No descongele las pechugas de pollo. Cena rápida, fácil y deliciosa😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">No descongele las pechugas de pollo. Cena rápida, fácil y
                                        deliciosa😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/f61T2hAohzY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/f61T2hAohzY/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLASVfk1PoN1D8DsDlgBqzsx_WgYiw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/f61T2hAohzY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¿Tienes 3 papas en casa? 🥔🥔🥔😱 Entonces esta receta es para ti 😉"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¿Tienes 3 papas en casa? 🥔🥔🥔😱 Entonces esta receta es para ti
                                        😉</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/JCGVI5yP-S4"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/JCGVI5yP-S4/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAwN2biOZEsE9Io539WvMwaZEcLeA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/JCGVI5yP-S4"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí colocas 3 pechugas de pollo...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí colocas 3 pechugas de pollo...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Gip8zXQFntM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Gip8zXQFntM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA8fApZat6PqNleIEjJYpw5J7TgJQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Gip8zXQFntM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Ahora solo preparo arroz así, mi familia me pide que lo vuelva a hacer😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Ahora solo preparo arroz así, mi familia me pide que lo vuelva a
                                        hacer😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/BGieje872eg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/BGieje872eg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDMssh7fm-5HJrIwwzUPlqZYF7KuA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/BGieje872eg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Todos van a mi negocio a comer este delicioso pollo mas rico que el KFC😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Todos van a mi negocio a comer este delicioso pollo mas rico que el
                                        KFC😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/8pC8Ot2kVHA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/8pC8Ot2kVHA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA55feyFXSC7wVmNyz-2B15VJMNvg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/8pC8Ot2kVHA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="El chef del KFC me revelo el secreto para que el pollo quede así de crujiente😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">El chef del KFC me revelo el secreto para que el pollo quede así de
                                        crujiente😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AyalbcZeTMQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/AyalbcZeTMQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCANYZ7qDYH6MRMvAmBqCr_Mq9U0g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AyalbcZeTMQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Solo 3 ingredientes y tu cena estará lista.😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Solo 3 ingredientes y tu cena estará lista.😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/hawSnTSMW1E"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/hawSnTSMW1E/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCjmloreZwFJl2nX4C0ymmnze-5Ww">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/hawSnTSMW1E"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Nunca me canso de comer esta deliciosa y económica ensalada!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Nunca me canso de comer esta deliciosa y económica
                                        ensalada!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">4.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/oRiYM3WDfuw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/oRiYM3WDfuw/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBk4LFFfnhIfGCrdr5yoZw5fsyAKQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/oRiYM3WDfuw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Rollitos de jamón y queso, prácticos, fáciles y deliciosos 😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Rollitos de jamón y queso, prácticos, fáciles y deliciosos
                                        😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/sW51OPZT5ik"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/sW51OPZT5ik/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAAjMo5Nn8uNR3i1sdt8x19DIu8YQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/sW51OPZT5ik"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí agregas una zanahoria rallada...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas una zanahoria rallada...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.7M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/vqz9zsLOAXw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/vqz9zsLOAXw/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAmf_YhUyDejgVTHRK7A8Ae77e-HA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/vqz9zsLOAXw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Me preguntaron porque las papas fritas me quedaron tan crujientes y sabrosas ¡Mira el secreto!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Me preguntaron porque las papas fritas me quedaron tan crujientes y
                                        sabrosas ¡Mira el secreto!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.7M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/UcwMvajHYNY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/UcwMvajHYNY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLClUgdhHkzxDW56fE0pf6lFlgcKbA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/UcwMvajHYNY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Todos van al negocio de mi hermano solo por esta receta de Zanahoria cremosa !Mira el secreto!❤️"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Todos van al negocio de mi hermano solo por esta receta de Zanahoria
                                        cremosa !Mira el secreto!❤️</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/u6pPeTSdeTc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/u6pPeTSdeTc/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBRw12HrB7HBhXttEPLm1X2EvEh-Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/u6pPeTSdeTc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gusta el plátano maduro es porque nunca te lo prepararon así.😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gusta el plátano maduro es porque nunca te lo prepararon
                                        así.😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/O5-0SqMfpLA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/O5-0SqMfpLA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBQLsGRFLY3HRqDFEVEBAHufMtjCw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/O5-0SqMfpLA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="En varias horas se acabarán los ratones, cucarachas y otros insectos en tu casa😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">En varias horas se acabarán los ratones, cucarachas y otros insectos
                                        en tu casa😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/CxVtcnQ51aI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/CxVtcnQ51aI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAUqTVd-tTW7ZHDJOksy_g2Q4FJ-w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/CxVtcnQ51aI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="LAS CAFETERÍAS NO QUIEREN QUE LO SEPAS. CAFE CAPUCHINO CREMOSO😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">LAS CAFETERÍAS NO QUIEREN QUE LO SEPAS. CAFE CAPUCHINO
                                        CREMOSO😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/11tewKp8Rp0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/11tewKp8Rp0/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCBlMfRqCuEbyPhd7yMiIy_cUjSyw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/11tewKp8Rp0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Ahora solo hago mozzarella en casa. ya no necesito comprar😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Ahora solo hago mozzarella en casa. ya no necesito
                                        comprar😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/n6gQD1qWEC8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/n6gQD1qWEC8/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBtUxhQSp5kUj82QOyf5cmXZX_ZFw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/n6gQD1qWEC8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="EL SECRETO DE LAS PALOMITAS MAS SABROSAS ¡YA NO COMPRO EN EL CINE!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">EL SECRETO DE LAS PALOMITAS MAS SABROSAS ¡YA NO COMPRO EN EL
                                        CINE!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/RUIyIVZG-nI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/RUIyIVZG-nI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCDndgID2VGjQvdtR5ChF24BUHr8Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/RUIyIVZG-nI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Ponle Sal a la Coca Cola y me lo agradecerás! ¡Es realmente increíble!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Ponle Sal a la Coca Cola y me lo agradecerás! ¡Es realmente
                                        increíble!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/TLb5Bydqm74"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/TLb5Bydqm74/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCt8WJF1O1dWYZvkWRxO3c4BunQSA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/TLb5Bydqm74"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Nunca has hecho esta receta de pollo con cerveza. ¡Se volverá la favorita de tu familia!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Nunca has hecho esta receta de pollo con cerveza. ¡Se volverá la
                                        favorita de tu familia!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/RsZgYSwFnmQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/RsZgYSwFnmQ/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCe0Er8EiaCe-fmMntx5xOt8WJaLg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/RsZgYSwFnmQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Pollo tan delicioso que lo cocino casi todos los días😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Pollo tan delicioso que lo cocino casi todos los días😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/CwWUyk2vMcY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/CwWUyk2vMcY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBKifglSNvLU1edmcYmlkSuCQloyg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/CwWUyk2vMcY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gustan las papas es porque nunca te las prepararon asi😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gustan las papas es porque nunca te las prepararon
                                        asi😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/krp1NFHT4Qk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/krp1NFHT4Qk/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB62qM0f1S1sSevq9MTtA8UReX0Uw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/krp1NFHT4Qk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="He mezclado las galletas maria con huevo ¡Secreto de las repostería!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He mezclado las galletas maria con huevo ¡Secreto de las
                                        repostería!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/_z2maCLE4wo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/_z2maCLE4wo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDWFjmZ8m_bq60zYdKuwxGFA89_IA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/_z2maCLE4wo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que si cortas 2 plátanos en rodajas finas...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que si cortas 2 plátanos en rodajas finas...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PMpNXi-STmM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PMpNXi-STmM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDTkyeihEKBcu7R25f_MLXDg9b0CA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PMpNXi-STmM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Después de este truco, Ya no tiro las cáscaras de ajo y cebolla!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Después de este truco, Ya no tiro las cáscaras de ajo y
                                        cebolla!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.7M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/TOZUDdeCXvs"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/TOZUDdeCXvs/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAWx2GPIisbg7bNwFOh2_hDMSgNmg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/TOZUDdeCXvs"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Mezcla café con plátano y te sorprenderás con el resultado😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mezcla café con plátano y te sorprenderás con el
                                        resultado😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.7M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PQBTmiaK4jU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PQBTmiaK4jU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD7WjfHsmYQ2Au6ZBnGeeSIVqdHDQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PQBTmiaK4jU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gusta el repollo es porque nunca te lo prepararon así😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gusta el repollo es porque nunca te lo prepararon
                                        así😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/0zMFL-UM6Rg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/0zMFL-UM6Rg/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD7Pkz0pqzVVIATEVYJ2Ihv3EoQ6w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/0zMFL-UM6Rg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gusta el sandwich es porque nunca te lo prepararon así😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gusta el sandwich es porque nunca te lo prepararon
                                        así😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/TeOwFHDbtCY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/TeOwFHDbtCY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCcd0LD-Qr-bR7XgRdQAsCUWrmGQQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/TeOwFHDbtCY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Desayuno listo en 5 minutos, usted querrá hacerlo todos los días!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Desayuno listo en 5 minutos, usted querrá hacerlo todos los
                                        días!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/WPDT1g-o6kc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/WPDT1g-o6kc/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA4IDW42cM15q2V4HmSLJFIOcdNdA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/WPDT1g-o6kc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="He mezclado la cáscara de piña con arroz ¡Secreto de las cafeterías!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He mezclado la cáscara de piña con arroz ¡Secreto de las
                                        cafeterías!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/yClYtOdzq2E"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/yClYtOdzq2E/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCXBnlQAh_zP-ObJ2T2H2PrXcEhhA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/yClYtOdzq2E"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí cortas una pechuga de...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí cortas una pechuga de...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/vI_m6ui_-zE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/vI_m6ui_-zE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAzRlelxkuJ8Xc3pke6xJ_ozpFPPw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/vI_m6ui_-zE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Añade la carne picada a las tortillas. ¡Que Rico! 😱🤤"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Añade la carne picada a las tortillas. ¡Que Rico! 😱🤤</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/D9APlXZO5Dk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/D9APlXZO5Dk/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDf317DkN567YPGFw4yFjNBl7shUQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/D9APlXZO5Dk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Cómo freír pescado con agua, Sin salpicaduras ni aceite quemado 😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Cómo freír pescado con agua, Sin salpicaduras ni aceite quemado
                                        😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/L7LEEtwKkmE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/L7LEEtwKkmE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDfHP2gdPYIeiYAkBCtZi70AbMMeg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/L7LEEtwKkmE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Mi casa huele rico, ya no tengo moscas ni mosquitos y sin gastar casi nada😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mi casa huele rico, ya no tengo moscas ni mosquitos y sin gastar
                                        casi nada😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/K9RoBLtTZwc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/K9RoBLtTZwc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAIvQKKL638kLK1u4QELVIJF7eSbg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/K9RoBLtTZwc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Vierte el café a la avena, un secreto que las cafeterías jamás revelan."
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Vierte el café a la avena, un secreto que las cafeterías jamás
                                        revelan.</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/eSwVQmbMiVM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/eSwVQmbMiVM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAINI_2t7Nw6o6_KDfXOCpqMa720A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/eSwVQmbMiVM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí cortas 2 plátanos en trozos...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí cortas 2 plátanos en trozos...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/pKGhxrdicbQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/pKGhxrdicbQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDhb5VAvXmVrPhDeG_94L3OBHMGIA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/pKGhxrdicbQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que al cortar una pechuga mediana...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al cortar una pechuga mediana...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AGRvlqGaiV0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/AGRvlqGaiV0/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDnqRelweiCnTR_tuho1BUAuxZy0A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AGRvlqGaiV0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Esta será la cena favorita de tu esposo, es muy fácil y rápida!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Esta será la cena favorita de tu esposo, es muy fácil y
                                        rápida!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">2M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/lBTJzHpU7pA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/lBTJzHpU7pA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDw3f7ZOmV8YmagXX3VjmvJc4GgTA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/lBTJzHpU7pA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí colocas una loncha de jamón...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí colocas una loncha de jamón...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/M5c6xvfsBo8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/M5c6xvfsBo8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCpSlWKC6vbNndfuKFnrHwyHYlXKQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/M5c6xvfsBo8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Esta masa ha encantado a todo el mundo y ¡es tan fácil de hacer!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Esta masa ha encantado a todo el mundo y ¡es tan fácil de
                                        hacer!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/LJ3XMNkvpOM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/LJ3XMNkvpOM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAFYxng3CRPHzwQn-v_BlRyO8keXQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/LJ3XMNkvpOM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Receta de un chef de restaurante 5 estrellas ¡Hoy la comparto con ustedes!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Receta de un chef de restaurante 5 estrellas ¡Hoy la comparto con
                                        ustedes!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/XCYBhcdzVKk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/XCYBhcdzVKk/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBgQhphtHFQtMNQ3Ng5Tt_HBHxgNQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/XCYBhcdzVKk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Agregue HUEVO a la leche hirviendo! Ya no compro en el mercado, con solo 3 ingredientes😱 ..."
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Agregue HUEVO a la leche hirviendo! Ya no compro en el mercado, con
                                        solo 3 ingredientes😱 ...</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Z2X4Yv19jJo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Z2X4Yv19jJo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAcVceODVpJO5HWfIOQIv43KUrV2Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Z2X4Yv19jJo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que al desmenuzar una pechuga...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al desmenuzar una pechuga...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/WJEAAYptawI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/WJEAAYptawI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDuak2GX41H4AN4LBCmBbUG7AcUQg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/WJEAAYptawI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que si añades una taza de arroz crudo a...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que si añades una taza de arroz crudo a...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/hUHNqGHJm2c"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/hUHNqGHJm2c/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB3k1BqFNaBYNAFlga412Cs-ltqwA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/hUHNqGHJm2c"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Poderoso shampoo natural que hará crecer tu cabello como nunca antes!"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Poderoso shampoo natural que hará crecer tu cabello como nunca
                                        antes!</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.9M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AvnKWxqvOdU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/AvnKWxqvOdU/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBKYHztqsFWmby4BnlTnRrhTHi0Zg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AvnKWxqvOdU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Mezclé arroz con plátano, el secreto de las barritas. #food #shorts #comida #receta #recetas"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mezclé arroz con plátano, el secreto de las barritas. #food #shorts
                                        #comida #receta #recetas</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/k5l0hhDGph8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/k5l0hhDGph8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLARKez_JUG42ccsUC5vOzszLpWfuw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/k5l0hhDGph8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Sabías que sí le haces varios cortes a dos pescados...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí le haces varios cortes a dos pescados...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/H1dFApg7Wds"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/H1dFApg7Wds/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAq0JjGvazEyOS5NaTbHdTqOxBukw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/H1dFApg7Wds"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Cómo freír pollo con agua, Sin salpicaduras ni aceite quemado😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Cómo freír pollo con agua, Sin salpicaduras ni aceite
                                        quemado😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/NX_p9J4r1Ok"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/NX_p9J4r1Ok/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDNcEGdvPxM85nh5X31Q4CiorFsqQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/NX_p9J4r1Ok"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¿Tienes medio kilo de papas en casa?🥔🥔😱 Entonces esta receta es para ti 😉"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¿Tienes medio kilo de papas en casa?🥔🥔😱 Entonces esta receta es
                                        para ti 😉</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.8M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/bh_j-214g9I"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/bh_j-214g9I/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB1U8fhNMnu0OpjWVqjovqyX9rtmg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/bh_j-214g9I"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Ponle coca cola a un aguacate y gracias por siempre! Quita el dolor"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Ponle coca cola a un aguacate y gracias por siempre! Quita el
                                        dolor</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.7M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/NGsDCBeV6xs"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/NGsDCBeV6xs/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDUBYk8nJR4_9eM7HT1YaSCzMIkEQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/NGsDCBeV6xs"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Las panaderías enloquecerán después de este video. Es muy simple y fácil de hacer😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Las panaderías enloquecerán después de este video. Es muy simple y
                                        fácil de hacer😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/4JFNeaM8unM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/4JFNeaM8unM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBKNsochgfRGVdK5fHLkgn0yTphFQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/4JFNeaM8unM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Sabías que al cortar finamente una pechuga mediana...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al cortar finamente una pechuga mediana...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/iXQMNv3wom8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/iXQMNv3wom8/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDqUH54xlzUjogdzZ6sL544seHY7w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/iXQMNv3wom8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Mezcla naranja con remolacha" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mezcla naranja con remolacha</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/e8pTHQYLRes"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/e8pTHQYLRes/oar2.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBjqG-k5DLBu4o6mcXJWaAfzI5PoA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/e8pTHQYLRes"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Cena rápida y económica que estará lista en unos minutos 🤤" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Cena rápida y económica que estará lista en unos minutos
                                        🤤</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/s7_yKj3j8Tg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/s7_yKj3j8Tg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCyaYp93rv4oMfy6Ccw-1yWo8kieQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/s7_yKj3j8Tg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Tomates con huevos de una forma nunca antes vista😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Tomates con huevos de una forma nunca antes vista😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ycm7_ln5464"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ycm7_ln5464/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD-36zzPvT4gIRGpumJXarlZU1QfQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ycm7_ln5464"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Esta es la receta que preparo para mi esposo cada fin de semana 😋🤭🍤"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Esta es la receta que preparo para mi esposo cada fin de semana
                                        😋🤭🍤</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PxPuq9Dp8Hw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PxPuq9Dp8Hw/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAUDbaIR0YVWuRJJyBcgfE4xHPkyA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PxPuq9Dp8Hw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Como hacer leche condensada casera en minutos ¡Con tan sólo 2 ingredientes!"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Como hacer leche condensada casera en minutos ¡Con tan sólo 2
                                        ingredientes!</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.4M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/pa0NzJhvDME"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/pa0NzJhvDME/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB2yNY69Fn_zD6MHeDeM_8W4laMhA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/pa0NzJhvDME"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Todos van al negocio de mi hermano solo por esta receta de Avena cremosa !Mira el secreto!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Todos van al negocio de mi hermano solo por esta receta de Avena
                                        cremosa !Mira el secreto!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ySwoM7ID-OA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ySwoM7ID-OA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCFEFeMBBmihhpGP91TY_g4Pr-Ixw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ySwoM7ID-OA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Ex empleado de McDonald's revela la receta de la salsa más deseada del mundo😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Ex empleado de McDonald's revela la receta de la salsa más deseada
                                        del mundo😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Qaj5MjQ4t_A"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Qaj5MjQ4t_A/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBzymaUopKNu9LDuhDQqA-n1EhcGA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Qaj5MjQ4t_A"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Mollejas de Pollo irresistibles tan buenas que las preparo casi a diario😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mollejas de Pollo irresistibles tan buenas que las preparo casi a
                                        diario😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.3M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/UmtHMoPTKCE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/UmtHMoPTKCE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDp2b4iJdeKXf0-SWH0ZvDifpkhCQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/UmtHMoPTKCE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí agregas una pechuga de pollo...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas una pechuga de pollo...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.6M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/kZLiuFiLV6M"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/kZLiuFiLV6M/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAF7rIeLgfzdWbY6kTNbrFZKhMfTQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/kZLiuFiLV6M"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que el café instantáneo...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que el café instantáneo...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.2M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/UBrlPq6sRcc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/UBrlPq6sRcc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCWerhfEAS3EHy4eWNOhJQvGOejPg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/UBrlPq6sRcc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí agregas zanahorias...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas zanahorias...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/-v2vFTCMhrI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/-v2vFTCMhrI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAKlLoYie1TNWqcH240gCWYRM2PnA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/-v2vFTCMhrI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Budín o Pudin de Pan receta fácil, rápida y buenísima 😱😋🍮" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Budín o Pudin de Pan receta fácil, rápida y buenísima
                                        😱😋🍮</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.5M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PGlLsiojYYM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PGlLsiojYYM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCW7j2em8cYNZRFolrUTI3CkcVAkA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PGlLsiojYYM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Sabías que al cortar finamente un pimiento mediano...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al cortar finamente un pimiento mediano...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Hc05mvXnMAw"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Hc05mvXnMAw/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLD0eUvbs5XYX_GvrFJq5mMPShk0nQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Hc05mvXnMAw"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Esta receta es fácil e increíblemente deliciosa. A todo el mundo le encantará 😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Esta receta es fácil e increíblemente deliciosa. A todo el mundo le
                                        encantará 😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ru7ktUc3WSQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ru7ktUc3WSQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAw5Vw4XqqQBC9bvpK3yhR8QAUT9A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ru7ktUc3WSQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Mayonesa casera, un secreto que las cafeterías jamás revelan." style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mayonesa casera, un secreto que las cafeterías jamás
                                        revelan.</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/54Bqj_Qf8eM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/54Bqj_Qf8eM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBVhp5x3cLkHBB9ASgNJsN1M7T4QQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/54Bqj_Qf8eM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="No puedo resistirme a ellas. ¡Sardinas super sabrosas y económicas!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">No puedo resistirme a ellas. ¡Sardinas super sabrosas y
                                        económicas!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/iGEByIfzJtU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/iGEByIfzJtU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLA737DH45ix891P9Qx9zWJbaI5DlA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/iGEByIfzJtU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que al cortar finamente una espinaca...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que al cortar finamente una espinaca...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/TUMdDMwjeo0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/TUMdDMwjeo0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB5AP8rN_aHBMr4fIipgrntsb6ecg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/TUMdDMwjeo0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Sabias que sí agregas medio kilo de carne picada a...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabias que sí agregas medio kilo de carne picada a...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/bFTgirH4NyU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/bFTgirH4NyU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCP7kaj2JTIj_hwStZVI-35p-omfA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/bFTgirH4NyU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¿Tienes papas en casa? 🥔🥔🥔😱 Entonces esta receta es para ti 😉"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¿Tienes papas en casa? 🥔🥔🥔😱 Entonces esta receta es para ti
                                        😉</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">998K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/p8wrQHKFP7Y"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/p8wrQHKFP7Y/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAJ-EpYny9mtVYXUOKfOchvo9r2FA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/p8wrQHKFP7Y"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Después de hacer Berenjena así, ¡ya no quiero carne! ¡Berenjena de una manera que nunca has visto!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Después de hacer Berenjena así, ¡ya no quiero carne! ¡Berenjena de
                                        una manera que nunca has visto!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/o_OOAisMejc"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/o_OOAisMejc/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCLmiqhW94xd-swW_lpMMQWdX7jCA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/o_OOAisMejc"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Esta manera de comer tomates ha cautivado a todos!😱 #recetas"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Esta manera de comer tomates ha cautivado a todos!😱
                                        #recetas</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">968K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/k7U5RbjZxjY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/k7U5RbjZxjY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAteNHfmgg31wzVeOmvwMm6dZ-xyw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/k7U5RbjZxjY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Mira lo que hice con esta piña que me sobro en casa 🤭"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Mira lo que hice con esta piña que me sobro en casa 🤭</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">954K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/buyUxxWoXg0"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/buyUxxWoXg0/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCDWeuOrcrdpLh34-yPfpKtL49dGA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/buyUxxWoXg0"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que si agregas 6 huevos al agua hirviendo...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que si agregas 6 huevos al agua hirviendo...😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">953K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/K9VY6yVY-SE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/K9VY6yVY-SE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDwa-jssDEwGmLcQMpe0PDjToEl_A">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/K9VY6yVY-SE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Con solo dos tomates, elabora esta deliciosa receta para el desayuno."
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Con solo dos tomates, elabora esta deliciosa receta para el
                                        desayuno.</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">941K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/KaGCjLqh1AM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/KaGCjLqh1AM/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBlTC8_iNqeO0SjXM11YH_lKEcm3Q">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/KaGCjLqh1AM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Después de que aprendí a hacer esta mezcla de condimentos, nunca volví a comprar en el mercado😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Después de que aprendí a hacer esta mezcla de condimentos, nunca
                                        volví a comprar en el mercado😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">938K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/myvABaf7o5M"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/myvABaf7o5M/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAC-zdbeuRNmvp2Y-XhLsJnSyhTJQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/myvABaf7o5M"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="La receta favorita de mi marido ¡es tan sabroso que lo hago todos los domingos!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">La receta favorita de mi marido ¡es tan sabroso que lo hago todos
                                        los domingos!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">938K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/HJe0R9Vm27s"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/HJe0R9Vm27s/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCDsA0J_RjKGf4KWwCXDTsQ7MDxhg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/HJe0R9Vm27s"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que si mezcla arroz...😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que si mezcla arroz...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">930K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/iygsuqBps1E"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/iygsuqBps1E/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDmwgs9w8qinRt4oSoXSdFIXl1gRg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/iygsuqBps1E"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Prepara carne molida sin esfuerzo ¡un sabor que te sorprenderá!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Prepara carne molida sin esfuerzo ¡un sabor que te
                                        sorprenderá!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">1.1M views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/pD1Kvs319Vg"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/pD1Kvs319Vg/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB-3YFvlPByA71RixN8wiobwfohgQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/pD1Kvs319Vg"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Cena lista en 3 minutos con esta mezcla de huevo y maíz! 🕒🍳🌽"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Cena lista en 3 minutos con esta mezcla de huevo y maíz!
                                        🕒🍳🌽</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">913K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/brNp4zXGFaA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/brNp4zXGFaA/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBBbjuKre--dUVoC3RP8PGivkcJ0g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/brNp4zXGFaA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="He mezclado pan viejo con huevo ¡Secreto de las repostería!😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He mezclado pan viejo con huevo ¡Secreto de las
                                        repostería!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">900K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ZgdMyB0tHc8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ZgdMyB0tHc8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAJIgODSpetX80q2d0foxN-tLKECg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ZgdMyB0tHc8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabias que si cortas dos bananas en...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabias que si cortas dos bananas en...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">879K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/qB3Kdhm-OCY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/qB3Kdhm-OCY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAcWj3f1GxyOBkA7wZBSje7paroNQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/qB3Kdhm-OCY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Con solo una papa y tres huevos tu cena estará lista 🤭" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Con solo una papa y tres huevos tu cena estará lista 🤭</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">775K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/yTwDBU-Ap-s"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/yTwDBU-Ap-s/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBwlrucYlaAX6DGbNF3AjGEJbxG4w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/yTwDBU-Ap-s"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Ya no hagas los huevos aburridos ¡Preparalos al estilo oriental!😍"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Ya no hagas los huevos aburridos ¡Preparalos al estilo
                                        oriental!😍</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">762K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PHQbtBr1bsU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PHQbtBr1bsU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCDYetym8U-qU1l1APZ2EmcNRc05w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PHQbtBr1bsU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí agregas pechuga de pollo...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas pechuga de pollo...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">744K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/PHz-9kdQmiU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/PHz-9kdQmiU/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDRtJtGyP7NepKyLxb8YfRbVu5_HA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/PHz-9kdQmiU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Huevos con tomates de una forma nunca antes vista😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Huevos con tomates de una forma nunca antes vista😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">718K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/grLevasnDfk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/grLevasnDfk/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAoNQ5nga5mEL2GJIv-xGkGMyxsRA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/grLevasnDfk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Con solo tres papas elabora esta receta para el desayuno😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Con solo tres papas elabora esta receta para el
                                        desayuno😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">707K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/h28N5NfpBMU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/h28N5NfpBMU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAUBWZIgm76OTU6tq9sVTDamAYrGA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/h28N5NfpBMU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="El dueño del restaurante me enseñó el secreto para hacer el mejor arroz con pollo. Fácil y rápido"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">El dueño del restaurante me enseñó el secreto para hacer el mejor
                                        arroz con pollo. Fácil y rápido</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">701K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/1aNxE4tmEgI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/1aNxE4tmEgI/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB61ke5wmefufuD7XV3-Yy0LTQqzg">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/1aNxE4tmEgI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Pollo con brócoli fácil y delicioso al estilo oriental😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Pollo con brócoli fácil y delicioso al estilo oriental😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">689K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/fc104dxF_50"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/fc104dxF_50/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLALiZ8SKVosqwuZ-iWB1hL9rBAQnw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/fc104dxF_50"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Aprende a hacer pasta perezosa sin ensuciar la sartén!😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Aprende a hacer pasta perezosa sin ensuciar la sartén!😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">673K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/gdbSmVV9nkE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/gdbSmVV9nkE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDjD5wOr81IDPasm99vL__G1B2FPA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/gdbSmVV9nkE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Pollo crujiente de una manera única y diferente. 😋🍗😲" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Pollo crujiente de una manera única y diferente. 😋🍗😲</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">671K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/FSa7I0dy8gk"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/FSa7I0dy8gk/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBOV9JKBZFGoeOMppeOa8_COCFg-g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/FSa7I0dy8gk"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Arroz tan delicioso que lo cocino casi todos los días! Muy fácil y económico😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Arroz tan delicioso que lo cocino casi todos los días! Muy fácil y
                                        económico😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">592K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/X1kqbyrUC4o"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/X1kqbyrUC4o/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLB0uQhnBXcHFPYwGK9U9cl4RhAO1g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/X1kqbyrUC4o"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gusta el sándwich es porque nunca te lo prepararon así. 🥪"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gusta el sándwich es porque nunca te lo prepararon así.
                                        🥪</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">556K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/HxdJLLQKUXQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/HxdJLLQKUXQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC01-UBbqLv11CtZfyd-JL-v1LFDQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/HxdJLLQKUXQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="2 patatas y tu cena estará lista en menos de 11 minutos 😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">2 patatas y tu cena estará lista en menos de 11 minutos
                                        😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">533K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/bQ0hQoycJ0k"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/bQ0hQoycJ0k/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAh0iCa8TH_4dhztmeoQ3Mimvoltw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/bQ0hQoycJ0k"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="He mezclado carne con huevo. ¡Secreto de cafeterías! 😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He mezclado carne con huevo. ¡Secreto de cafeterías! 😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">532K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Htgm0jd0xE8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Htgm0jd0xE8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAVOZycZs9LZqRmw8ikuGW5YLYaqw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Htgm0jd0xE8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Añade huevos a los espaguetis y sorpréndete con el resultado. ¡Tienes que probarlo!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Añade huevos a los espaguetis y sorpréndete con el resultado.
                                        ¡Tienes que probarlo!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">552K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/HBJZb9IjItU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/HBJZb9IjItU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBiQFtk--7oIkLZfgdm0CwiXoWLtw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/HBJZb9IjItU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Como hacer una Torta de Naranja casera. Receta detallada paso a paso"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Como hacer una Torta de Naranja casera. Receta detallada paso a
                                        paso</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">542K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/AdSbRpugWMM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/AdSbRpugWMM/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBU9Fr2WYcaZEYCdFfzUZeUb_KGJA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/AdSbRpugWMM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Pelaste mal los huevos cocidos toda tu vida y no lo sabías.😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Pelaste mal los huevos cocidos toda tu vida y no lo
                                        sabías.😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">487K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/Lomk3UJIJpI"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/Lomk3UJIJpI/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAF4NtI4FrwLZX4E7GB5KHgVjZv9w">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/Lomk3UJIJpI"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="¡El Postre de Piña con Solo 3 Ingredientes!🍍🍍"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡El Postre de Piña con Solo 3 Ingredientes!🍍🍍</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">474K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/32rzoDpLVcQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/32rzoDpLVcQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBWKizypHJ1wWd7TWPHuVDgJfUDhQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/32rzoDpLVcQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Cuando preparo esta deliciosa bebida, todos me piden la receta!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Cuando preparo esta deliciosa bebida, todos me piden la
                                        receta!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">457K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/NBTf-0UciYo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/NBTf-0UciYo/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLAeA9Mdqkqts7_cBOUzktYXAfeiRA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/NBTf-0UciYo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Sabías que sí agregas una zanahoria rallada en un recipiente...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas una zanahoria rallada en un
                                        recipiente...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">475K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ipi8d5zhiQU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ipi8d5zhiQU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC6hnnvO6Wr-XIIoBqSfRZTt-3vPA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ipi8d5zhiQU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Esta ensalada de aguacate es tan deliciosa y saludable que la hago una y otra vez! 🥗"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Esta ensalada de aguacate es tan deliciosa y saludable que la hago
                                        una y otra vez! 🥗</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">422K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/VznYw_gx9E8"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/VznYw_gx9E8/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCK8jqnx9-Xc8Ruz2fVjN_VHqK7Ig">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/VznYw_gx9E8"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si tienes dos latas de atún en casa, prueba esto ¡Un secreto que pocos conocen!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si tienes dos latas de atún en casa, prueba esto ¡Un secreto que
                                        pocos conocen!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">426K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/ESHLkwBHhLY"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/ESHLkwBHhLY/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLC58zRuyhzsYyBfstQt3UMyqGJLXw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/ESHLkwBHhLY"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Los niños me piden que lo haga casi todos los días! 🍗🤭" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Los niños me piden que lo haga casi todos los días! 🍗🤭</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">398K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/1FqSYxNxAqQ"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/1FqSYxNxAqQ/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBLnPyeC7T5sIyAEeYsaK0_tJl7aQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/1FqSYxNxAqQ"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que si colocas pasta para lasaña...😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que si colocas pasta para lasaña...😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">415K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins="" is-slim-media=""
        is-in-first-column=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/hebrXnIjeDA"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/hebrXnIjeDA/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLDj9Lweafq4MH5pL5KvUsvywoXG8g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/hebrXnIjeDA"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Si no te gusta la carne molida es porque nunca te lo prepararon así. 🥩🥩"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Si no te gusta la carne molida es porque nunca te lo prepararon así.
                                        🥩🥩</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">360K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/D_bXy9uXfgM"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/D_bXy9uXfgM/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCxbOy5CK-6AfcsdEktRTkWF3su_g">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/D_bXy9uXfgM"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Pan Relleno - ¡El Desayuno Más Increíble Que Has Visto!😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Pan Relleno - ¡El Desayuno Más Increíble Que Has Visto!😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">356K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/3NZRsWJ57LU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/3NZRsWJ57LU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLBQLcht6Z63op8Y39QgWuWTyKUJyQ">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/3NZRsWJ57LU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false" title="Sabías que sí agregas azúcar a la sartén…😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Sabías que sí agregas azúcar a la sartén…😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">348K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/dj5lWMXoQFU"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/dj5lWMXoQFU/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCNRfs60k57SPlbhW9s-_KtXH2xTw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/dj5lWMXoQFU"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="Una cena rápida y deliciosa con solo 1 papa y 3 huevos.😱" style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">Una cena rápida y deliciosa con solo 1 papa y 3 huevos.😱</span></a>
                            </h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">335K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer><ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/JCYXQsLU3Jo"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/JCYXQsLU3Jo/hq720.jpg?sqp=-oaymwEoCJUDENAFSFryq4qpAxoIARUAAIhC0AEB2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCNEnFG9GsrSrSwpBFfjFjEm7RBZA">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/JCYXQsLU3Jo"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="He mezclado la pulpa de maracuyá con huevo ¡Secreto de las repostería!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">He mezclado la pulpa de maracuyá con huevo ¡Secreto de las
                                        repostería!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">333K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer>
    <ytd-rich-item-renderer class="style-scope ytd-rich-grid-renderer" items-per-row="4"
        lockup="true" rendered-from-rich-grid="" is-shorts-grid="" no-gutter-margins=""
        is-slim-media=""><!--css-build:shady--><!--css_build_scope:ytd-rich-item-renderer--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js-->
        <div id="content" class="style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model-v2
                class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><ytm-shorts-lockup-view-model
                    class="shortsLockupViewModelHost style-scope ytd-rich-item-renderer"><a href="/shorts/4RXSsdPZcsE"
                        class="shortsLockupViewModelHostEndpoint reel-item-endpoint" aria-haspopup="false" tabindex="-1"
                        aria-hidden="true" style="">
                        <div
                            class="shortsLockupViewModelHostThumbnailParentContainer shortsLockupViewModelHostThumbnailParentContainerRounded">
                            <div
                                class="shortsLockupViewModelHostThumbnailContainer shortsLockupViewModelHostThumbnailContainerAspectRatioTwoByThree">
                                <img alt=""
                                    class="ytCoreImageHost shortsLockupViewModelHostThumbnail ytCoreImageFillParentHeight ytCoreImageFillParentWidth ytCoreImageContentModeScaleAspectFill ytCoreImageLoaded"
                                    src="https://i.ytimg.com/vi/4RXSsdPZcsE/oardefault.jpg?sqp=-oaymwEoCJUDENAFSFqQAgHyq4qpAxcIARUAAIhC2AEB4gEKCBgQAhgGOAFAAQ==&amp;rs=AOn4CLCai1iSOZcgwy_H-rnVRQRB5qIXRw">
                            </div>
                        </div>
                    </a>
                    <div role="presentation"
                        class="shortsLockupViewModelHostOutsideMetadata shortsLockupViewModelHostMetadataRounded shortsLockupViewModelHostOutsideMetadataHasMenu">
                        <div>
                            <h3 role="presentation"
                                class="shortsLockupViewModelHostMetadataTitle shortsLockupViewModelHostOutsideMetadataTitle">
                                <a href="/shorts/4RXSsdPZcsE"
                                    class="shortsLockupViewModelHostEndpoint shortsLockupViewModelHostOutsideMetadataEndpoint"
                                    aria-haspopup="false"
                                    title="¡Solo leche, huevos y plátanos, sin horno, sin harina! ¡Te Sorprenderá lo rico que queda!😱"
                                    style=""><span
                                        class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                        role="text">¡Solo leche, huevos y plátanos, sin horno, sin harina! ¡Te
                                        Sorprenderá lo rico que queda!😱</span></a></h3>
                            <div
                                class="shortsLockupViewModelHostOutsideMetadataSubhead shortsLockupViewModelHostMetadataSubhead">
                                <span class="yt-core-attributed-string yt-core-attributed-string--white-space-pre-wrap"
                                    role="text">349K views</span></div><span></span>
                        </div>
                        <div
                            class="shortsLockupViewModelHostOutsideMetadataMenu shortsLockupViewModelHostShowOverPlayer image-overlay-text">
                            <button
                                class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--enable-backdrop-filter-experiment"
                                title="" aria-label="More actions">
                                <div aria-hidden="true" class="yt-spec-button-shape-next__icon"><span
                                        class="ytIconWrapperHost" style="width: 24px; height: 24px;"><span
                                            class="yt-icon-shape ytSpecIconShapeHost">
                                            <div style="width: 100%; height: 100%; display: block; fill: currentcolor;">
                                                <svg xmlns="http://www.w3.org/2000/svg"
                                                    enable-background="new 0 0 24 24" height="24" viewBox="0 0 24 24"
                                                    width="24" focusable="false" aria-hidden="true"
                                                    style="pointer-events: none; display: inherit; width: 100%; height: 100%;">
                                                    <path
                                                        d="M12 16.5c.83 0 1.5.67 1.5 1.5s-.67 1.5-1.5 1.5-1.5-.67-1.5-1.5.67-1.5 1.5-1.5zM10.5 12c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5zm0-6c0 .83.67 1.5 1.5 1.5s1.5-.67 1.5-1.5-.67-1.5-1.5-1.5-1.5.67-1.5 1.5z">
                                                    </path>
                                                </svg></div>
                                        </span></span></div><yt-touch-feedback-shape aria-hidden="true"
                                    class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--touch-response">
                                    <div class="yt-spec-touch-feedback-shape__stroke"></div>
                                    <div class="yt-spec-touch-feedback-shape__fill"></div>
                                </yt-touch-feedback-shape>
                            </button></div>
                    </div>
                </ytm-shorts-lockup-view-model></ytm-shorts-lockup-view-model-v2></div>
        <yt-interaction id="interaction" class="extended rounded-large style-scope ytd-rich-item-renderer"
            hidden=""><!--css-build:shady--><!--css_build_scope:yt-interaction--><!--css_build_styles:video.youtube.src.web.polymer.shared.ui.styles.yt_base_styles.yt.base.styles.css.js,video.youtube.src.web.polymer.shared.ui.yt_interaction.yt.interaction.css.js-->
            <div class="stroke style-scope yt-interaction"></div>
            <div class="fill style-scope yt-interaction"></div>
        </yt-interaction>
    </ytd-rich-item-renderer></div>"""  # aquí pegas el HTML
base_url = "https://www.youtube.com"

soup = BeautifulSoup(html, "html.parser")

short_links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    if href.startswith("/shorts/"):
        full_url = base_url + href
        if full_url not in short_links:
            short_links.append(full_url)

# Guardar en un archivo txt
save_links_to_txt(short_links, "shorts_links.txt")

print("✅ Links guardados en shorts_links.txt")
